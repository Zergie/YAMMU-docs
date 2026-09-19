"""Build a filtered wiki commit; print its SHA without changing any branch."""
import os
from pathlib import Path
import re
import subprocess
import tempfile


def git(*args, input=None, env=None):
    return subprocess.check_output(['git', *args], input=input, env=env)


def ancestor(older, newer):
    result = subprocess.run(['git', 'merge-base', '--is-ancestor', older, newer])
    if result.returncode not in (0, 1):
        raise RuntimeError('Cannot inspect commit ancestry')
    return result.returncode == 0


def filtered_tree(commit):
    # A private index keeps the checkout and real index untouched. Git itself
    # interprets .wikiignore, including **, anchored paths, comments and ! rules.
    with tempfile.TemporaryDirectory() as directory:
        env = dict(os.environ, GIT_INDEX_FILE=str(Path(directory) / 'index'))
        git('read-tree', commit, env=env)
        rules = Path(directory) / 'excludes'
        has_rules = git('ls-tree', '--name-only', commit, '--', '.wikiignore').strip()
        rules.write_bytes(git('show', f'{commit}:.wikiignore') if has_rules else b'')
        excluded = git('ls-files', '--cached', '--ignored', '-z',
                       f'--exclude-from={rules}', env=env)
        if excluded:
            git('update-index', '--force-remove', '-z', '--stdin', input=excluded, env=env)
        return git('write-tree', env=env).decode().strip()


def main():
    source = git('rev-parse', 'HEAD').decode().strip()
    wiki = git('rev-parse', 'refs/remotes/wiki/master').decode().strip()
    # The original exact mirror (or a manually reconciled wiki) is an ancestor
    # of main. Subsequent filtered publications have a source trailer instead.
    if not ancestor(wiki, source):
        message = git('show', '-s', '--format=%B', wiki).decode()
        markers = re.findall(r'^YAMMU-Docs-Source: ([0-9a-f]{40})$', message, re.M)
        if len(markers) != 1 or not ancestor(markers[0], source):
            raise SystemExit('Wiki has unmerged edits or main history changed. Merge wiki/master into main before publishing.')
        previous_tree = filtered_tree(markers[0])
        if previous_tree != git('rev-parse', f'{wiki}^{{tree}}').decode().strip():
            raise SystemExit('Wiki content differs from its recorded source. Merge wiki/master into main before publishing.')

    tree = filtered_tree(source)
    if not git('ls-tree', '-r', '--name-only', tree).strip():
        raise SystemExit('Refusing to publish an empty wiki; check .wikiignore.')
    if tree == git('rev-parse', f'{wiki}^{{tree}}').decode().strip():
        print(wiki)  # Ignored-only changes do not create empty wiki commits.
        return
    message = f'Publish YAMMU docs {source[:12]}\n\nYAMMU-Docs-Source: {source}\n'
    print(git('commit-tree', tree, '-p', wiki, input=message.encode()).decode().strip())


if __name__ == '__main__':
    main()
