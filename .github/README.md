# YAMMU documentation

Contribute to the [YAMMU wiki](https://github.com/Zergie/YAMMU/wiki) by editing
pages in this repository and opening a pull request against `main`.

## Repository-only files

List paths in the root `.wikiignore` to keep them tracked here but exclude them
from the published wiki. Rules use Git's gitignore syntax, independently of
`.gitignore`: comments, wildcards, `**`, leading `/`, directories and `!` exceptions.
Patterns without a slash match at any depth; a leading `/` anchors to the root.
As with gitignore, a file cannot be re-included while its parent directory is excluded.

Defaults exclude `.github/`, root README/CONTRIBUTING files, `.wikiignore`,
`.gitignore`, agent instructions (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`), and
`skills/`, `.agents/`, `.claude/`, `.codex/` directories at any depth.
This covers `.github/skills/`, `.agents/skills/` and `.claude/skills/` too.
Edit these rules if any of those names should be actual wiki content.

Example:

```gitignore
/internal-notes/
**/draft-*.md
```

## Publishing

Pushes to `main` and manual runs of **Actions → Publish wiki** publish the latest
filtered snapshot to `Zergie/YAMMU.wiki.git`, branch `master`. Only tracked files
are considered. Binary assets and file modes are preserved. Deletions and newly
ignored files are removed from the current wiki tree; old history is retained.
Ignored-only changes create no wiki commit. Ignore rules do not remove previously
published material from Git history and should not be used to hide secrets.

Wiki commits have their own IDs and record the source commit in a
`YAMMU-Docs-Source` trailer. Runs are serialized and always use the latest `main`,
so a single publication may include multiple source commits. The original wiki's
19 commits have already been imported into this repository.

The workflow never force-pushes. If somebody edits the wiki directly, publication
stops. Fetch its `master` branch and merge it into `main` through a pull request,
resolving any conflicts, then rerun publication. Concurrent wiki updates also
cause the push to fail safely. An empty filtered wiki is rejected.

## Credentials

Add an Actions repository secret named `WIKI_TOKEN` with credentials that can push
to the YAMMU wiki. A classic personal access token with `public_repo` scope can be
used for this public wiki. Do not commit the token. Then manually run **Publish wiki**.
The source repository's `GITHUB_TOKEN` only needs `contents: read`.
