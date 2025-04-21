# InvenTree project

InvenTree project wide docs and tools.
This covers both ADRs for [InvenTree/InvenTree](https://github.com/inventree/) as well as other systems in the [InvenTree org](https://github.com/inventree/).

## Tech stack

- pre-commit (config and in CI) to ensure common formatting and spellchecking
- uv for managing environments, dependencies and packaging
- adr-viewer for rendering the docs

## Structure

- `.github` - contains the CI/CD configs
- `docs/adr` - contains the ADRs for the InvenTree project
- `doc-builder` - contains the stuff needed for sphyinx to build the docs
