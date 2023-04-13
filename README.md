# Prefect Versioned Documentation

This repository contains Prefect's versioned documentation. Development of the docs 
happens in the main Prefect repository, so if you're looking to edit or add 
documentation, https://github.com/PrefectHQ/prefect/tree/main/docs is where you want 
to be. 

The `docs` repository serves two purposes:
1. Build versioned documentation via a GitHub action. 
2. Make versioned docs available for publishing via Netlify. 

## How it works

First, the docs build action is triggered, either manually or by an automatic 
repository dispatch call from the `PrefectHQ/prefect` repository.

## Manual docs builds
Manually triggered builds accept two parameters: 
  - A version
  - An optional display name that's displayed in the version selector box.

### Choosing version and display name
If you don't provide a version name, the build action uses the version as the display 
name. In most cases, this is what you want. If you're building the docs for `2.10.4`, 
for example, you probably want them published as `2.10.4`. In that scenario, entering
`2.10.4` as the version and leaving the display name blank will provide what's needed.

But sometimes, you might want to publish a docs version under an alias. For example, it 
might be better to combine the docs for older releases to keep the number of versions 
in the selector manageable. 

So, if you know that the docs for `2.6.12` are useful for the entire series of `2.6` 
releases, you might decide to build the docs for `2.6.12` but publish them as `2.6.x`.

### Merging and deploying manual builds
When a manual docs build completes, the build action will create a pull request that
must be reviewed by a human and merged into the `main` branch. 

An updated copy of the website is deployed to Netlify every time a merge to `main` 
occurs and the updated docs usually appear at https://docs.prefect.io in under a minute.

## Automated docs builds
- 1
- 2

### Build triggers
- 1
- 2

### Merging and deploying automated builds
- 1
- 2