# 00 – Project Startup Checklist (Python Data Project)

> Fill the blanks, work top-to-bottom, then delete this file when done.

**Project name:** ________     **Package (PKG_NAME):** ________     **Repo URL:** ________

---

# Steps
## 1. Repo basics
- [ ] Verify template copied correctly (no stray `PKG_NAME` placeholders)
- [ ] Set package folder name: `src\<PKG_NAME>
- [ ] Update `pyproject.toml` -> `[project].name = "<PKG_NAME>"`
- [ ] Update `pipeline\run_pipeline.py` -> "PKG_NAME"

## 2. Git init & first commit
```powershell
git init -b main
git add .
git commit -m "init: initial commit"
```

## 3. GitHub
- Create github remote
```powershell
gh repo create <your-username>/<repo-name> --private --source . --remote origin --push
```
- protect `main`
`Set-GitHubBranchProtection <your-username> <repo-name> <branch-name>`

## 3b. Set Python version with pyenv-win
- ensure pyenv is available -> `pyenv --version`
- get current python version -> `python -V`
- confirm I'm using the shim ->    `Get-Command python | Select-Object -Expand Source`
- write python version to .python-version file
`pyenv local (python -c "import platform; print(platform.python_version())")`

## 4. Virtual Environment
```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -V
```

## 5. Install tooling + editable package
```powershell
python -m pip install -U pip setuptools wheel
pip install -e
pip install pre-commit black ruff pytest
pre-commit install
```

## 6. Configs & secrets
- Open `configs/base.yml` and set:
    - [ ]`runtime.as_of_date` -> today's date or desired date run
    - [ ] `input_dir` / `outpub_dir` -> 
- Place any local-only creds in `configs/secrets/` (git-ignored)

## 7. data/outputs folders (sanity check)
- [ ] `data/raw/`, `data/interim/`, `data/processed/` exist
- [ ] `data_samples/` has at least one tiny fabricated CSV
- [ ] `output/reports`, `output/figures`, `output/exports` exist

## 8. Smoke tests
```powershell

pytest -q
python -c "import <PKG_NAME>; print('import ok')"
python pipelines/run_pipeline.py # should print something harmless

## 9. CI (optional)
- [ ] `.github/workflows/ci.yml` exists
- [ ] In GitHub Branch Protection, require status check named **ci** (match job name)
- [ ] Push and open a PR to verify CI runs:
```powershell

git switch -c chore/ci-smoke
# (edit README or small change)
git add .; git commit -m "chore(ci): add CI smoke test"
git push -u origin chore/ci-smoke
gh pr create --fill
# after CI passes:
gh pr merge --squash
```

## 10. Working conventions (keep it tight)
- Branch names: `feat/<desc>`, `fix/<desc>`, `chore/<desc>`, `docs/<desc>`, `refact/<desc>`, `style/<desc>`, `test/<desc>`, `hotfix/<desc>`
- Commit msgs: 50-char title; body wraps at 72 chars
- GitHub Flow: small branches -> PR -> squash-merge to `main`

## 11. First real task
- [ ] Create branch for your first unit of work
```powershell
git switch -c <branch-name>
```
- [ ] Explore in `notebooks/`, then promote reusable code into `src/PKG_NAME`
- [ ] Add/adjust tests in `tests/`
- [ ] Self-PR, CI, squash-merge to `main`

----------------------------------------------------------------

# Quick reference
- Activate .venv `.\.venv\Scripts\activate`
- Lint/format (after pre-commit is installed): happens on commit
- Run tests: `pytest -q`
- Run pipeline: `python pipelines\run_pipeline.py`
- Editable install (once per fresh clone): `pip install -e`
