# Prefect Versioned Documentation

This repository contains Prefect's versioned documentation. Development of the docs 
happens in [the `docs` directory](https://github.com/PrefectHQ/prefect/tree/main/docs) 
of the main Prefect repository, so any edits or additions should be done there.

The `docs` repository serves two purposes:
1. Build versioned documentation via a GitHub action. 
2. Make versioned docs available for publishing via Netlify. 

## How it works

First, the docs build action is triggered, either manually or by an automatic 
repository dispatch call from the `PrefectHQ/prefect` repository.

Next, the build happens in the [build workflow action](https://github.com/PrefectHQ/docs/blob/main/.github/workflows/build-docs.yaml).

To keep things simple, the workflow primarily consists of Bash commands that clone the a
branch or release tag of [the Prefect repository](https://github.com/PrefectHQ/prefect),
prepare it for the `mike` build utility, sort the versions list `mike` generates, and 
then create a pull request to merge the changes into `main`.

The workflow calls several small Python scripts in the `utilities` directory to handle
scripts handle preparation steps that would be difficult or verbose in bash.

## Manual docs builds
Manually triggered builds accept two parameters: 
  - A version
  - An optional display name that's displayed in the version selector box.

### Choosing version and display name
If you don't provide a version name, the build action uses the version as the display 
name. In most cases, this is what you want. If you're building the docs for `2.10.4`, 
for example, you probably want them published under the name `2.10.4`. 

In that scenario, entering `2.10.4` as the version and leaving the display name blank 
will build the docs for Prefect `2.10.4` and publish them as `2.10.4` - exactly what 
you want.

However, you may occasionally want to publish a docs version under an alias. 
For example, it might be better to combine the docs for older release series under a 
single name to keep the length of the version selector box manageable.

So, if you know that the docs for `2.6.12` are useful for the entire series of `2.6` 
releases, you might decide to build the docs for `2.6.12` but publish them as `2.6.x`.

### Merging and deploying manual builds
When a manual docs build completes, the build action will create a pull request that
must be reviewed by a human and merged into the `main` branch. 

An updated copy of the website is deployed to Netlify every time a merge to `main` 
occurs and the updated docs usually appear at https://docs.prefect.io in under a minute.

## Automated docs builds
Automated docs builds run in response specific changes to in the Prefect repository. 

The events in the Prefect repo that trigger a versioned docs build in _this_ repository
are:
- A new release is published
- A change to the `docs` directory is merged to main
- A change to `netlify.toml` is merged to main


### Merging and deploying automated builds
Automated builds create auto-merge pull requests, so no human intervention should be 
required unless something goes wrong. 

If the docs site isn't updating in response to 
changes that _should_ trigger a new build, check the [list of recent build workflow
runs](https://github.com/PrefectHQ/docs/actions/workflows/build-docs.yaml) for build failures.

## `unreleased` docs version
The versioned docs currently show an `unreleased` version in the version selector. 
This version includes the latest docs changes from the main branch of the `prefect` 
repository. 

To hide the unreleased docs, do the following:
- Change `HIDE_UNRELEASED_VERSION` to `True` in `sort-docs-versions.py`.
- Delete the `unreleased` version from `versions/versions.json`.
- Push the changes to the `main` branch of this repository.