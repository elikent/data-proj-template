# Project root
## pyproject.toml
Project settings. Tells `pip` where my code lives, sets name/version, and tool configs and CLI entry points.
*Use when:* rename the package, add a CLI or add tool settings (black/ruff/pytest)

## README.md
What project does and quick-start
*Use when:* keep install/run steps accurate

## CHANGELOG.md
Human-readable history of notable changes (version/date + bullets)
*Use when:* tag a release or ship a meaningful change

## .env.example
Template for required env vars (no secrets)
*Use when:* add a new credential/config - document here

# Source Code
## src/PKG_NAME
Importable code

## src/PKG_NAME/init.py
Package "front door." Optionally re-export a small public API.

## src/PKG_NAME/cli.pu
Optional command entry point (`[project.scripts]` in pyproject)

## src/PKG_NAME/ingest
Download/fetch code (paginations, retries, backoff)
*Use when:* pulling data from APIs/files into `data/raw`

## src/PKG_NAME/transform
Cleaning, parsing, joins, field mapping
*Use when:* turning raw into shaped tables / DataFrames

## src/PKG_NAME/validate
Data contracts (pandera/pydantic), invariants
*Use when:* enforcing schema/quality gates before writing outputs

## src/PKG_NAME/io
Centralized read/write helpers, path builders (CSV/Parquet)
*Use when:* standardizing I/O and keeping file login in one place

# Other dirs
## tests/test_smoke.py
Minimal sanity test to prove imports and a simple function work

## pipelines/run_pipeline.py
This runner/orchestrator (reads configs, calls `src` functions)
*Use when:* kicking off the ETL/ELT end-to-end locally or via scheduler

## configs/base.yml
Central runtime config (paths, dates, parameters)
*Use when:* changing input/output locations, dates, toggles - never hardcode in code

## configs/secrets
Store real secrets here. Directory is included in .gitignore

## data/external
small, stable datasets my scripts rely on (e.g. states/state-codes)

## data/raw
Read-only data inputs

## data/interim
Scratch/staged artifacts; safe to delete/rebuild

## data/processed
Clean, ready-to-use datasets for downstream use

## output/reports
PDFs, Markdowns, HTML deliverables

## output/figures
Charts, plots, images

## output/exports
CSV/XLSX extracts for stakeholders

