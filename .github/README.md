# YAMMU documentation

Community contributions to the [YAMMU wiki](https://github.com/Zergie/YAMMU/wiki).

## Contributing
Edit the Markdown pages in the repository root and open a pull request against `main`.
Keep existing filenames and wiki links intact unless a rename is intentional.
After a merge or direct push to `main`, GitHub Actions publishes the same commits to
`Zergie/YAMMU.wiki.git` on `master`.

Please make documentation changes here. Direct wiki edits must be merged back into
`main` before publishing can resume; the workflow never force-pushes.

## Initial setup
The first workflow run imports the existing wiki, including its complete Git history.
It can complete that import even before publishing credentials are configured.

Add an Actions repository secret named `WIKI_TOKEN` with a token owned by an account
that can push to the YAMMU wiki. For this public wiki, a classic personal access token
with the `public_repo` scope can be used. Treat it as a credential: do not commit it.
The default `GITHUB_TOKEN` belongs to YAMMU-docs and does not grant access to YAMMU.

After adding the secret, open Actions → Publish wiki → Run workflow on `main`.
Repository settings must allow GitHub Actions and the workflow's `contents: write`
permission for the initial import. Once imported, publication needs only read access
to YAMMU-docs; `contents: write` can be reduced to `contents: read`.

## Sync behavior
Runs are serialized and publish the latest `main`, including all preceding commits.
The target wiki branch is `master`; the source branch is `main`.
The workflow performs only fast-forward wiki pushes. Divergence produces an error.
If you edit the wiki directly, fetch its `master` branch, merge it into `main`
through a pull request, then run publication again.

The workflow configuration and this guide live under `.github/` so the repository
root remains dedicated to wiki pages. Exact commit mirroring includes these files.
