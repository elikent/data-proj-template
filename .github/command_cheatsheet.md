# Workflow
1. Sync main
- `git switch main`
- `git pull --ff-only`

2. Branch for the new task
- `git switch -c <branch-type/desc>` # fix, chore or feat (docs, style, refactor, test)

3. Small chunks and commit often
- run checks before each commit: `pre-commit run --all-files && pytest -q`
- `git add <paths> && git commit --amend --no-edit` # when continuing work on same task without a new push

4. Keep branch current
- `git fetch origin`
- `git rebase origin/main`

5. Push
- `git push -u origin <branch-name>`

6. Open PR
- `gh pr create --fill --base main --head <branch-name>` 
# --fill: auto-fills commit msgs
# --base main = target branch
# --head <branch-name> = source branch 

7. Merge (squash)
- `gh pr merge --squash --delete-branch`
# -- combines all commits from PR into one commit on main

# Other useful commands
## Inspect & status
- `git status`
- `git remove -v` # (gives origin for fetch and push)
- `git branch`
- `git branch -r` # remote branches
- `git rev-parse --abbrev-ref HEAD` # gives branch where HEAD is pointed
- `git show HEAD` # show last commit (diff + metadata)

## History & search
- `git log --oneline --decorate --graph --all`  # this is pretty unclear to me
- `git log -p <path>`                           # history with patches for a file
- `git log -S "string"`                         # search code changes containing string"
- `git blame <path>`                            # who last changed each line

## Diff & stage
- `git diff`                    # show unstaged changes
- `git restore <path>`          # discard working-tree changes to a file
- `git add -p`                  # interactively stage hunks
- `git restore --staged <path>` # unstage a file

## Undo & fix (safe-first)
- `git commit --amend`  # edit last commit (message or staged files)
- `git restore <path>`  # discard working-tree changes to file
- `git revert <commit>` # make a new commit that undoes <commit> (reverts are safest for published history)

### Resets (use carefully)
- `git reset --soft <commit>`   # keep changes staged
- `git reset --mixed <commit>`  # keep changes, unstage them (default)
- `git reset --hard <commit>`   # discard changes; set HEAD/WT to <commit>
- `git clean -fd`   # remove untracked files/dirs (dangerous)

## Tracking & Upstream
- `git push -u origin my-branch`            # set upstream on first push
- `git branch -u origin/my-branch`          # set upstream for existing branch
- `git fetch --all --prune`                 # update remotes, drop deleted refs

## Remotes
- 