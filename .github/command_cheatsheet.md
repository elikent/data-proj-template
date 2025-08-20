# Workflow
1. Sync main
- `git switch main`
- `git pull --ff-only`
- `git fetch --prune` # keeps origin/ * tidy locally 

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

## If worked on main by accident
1. Move local commit(s) off main 
- `git switch -c chore/move-off-main`

2. Reset local to match remote 
- `git switch main`
- `git fetch origin`
- `git reset --hard origin/main`

3. PR the branch back into main
- `git switch chore/move-off-main` 
- `gh pr create --fill --base main --head chore/move-off-main`
- `gh pr merge --squash --delete-branch`

4. Sync local main
- `git switch main`
- `git pull --ff-only`
- `git fetch --prune` # keeps origin/ * tidy locally 

# Aliases
## One-time
```bash
git config --global user.name "Your Name"
git config --global user.email "Your Email"
git config --global init.defaultBranch main
git config --global pull.ff only
```

```bash
git config --global alias.lg log --oneline --decorate --graph --all
git config --global alias.nb "switch -c"
git config --global alias.sw "switch"

# Other most useful commands
## See where you are
- `git status`
- `git remote -v` # (gives origin for fetch and push)
- `git branch`
- `git branch -r` # remote branches in local list
- `git ls-remote --heads origin` # remote branches in remote list
- `git fetch --prune` # update and prune stale remote-tracking branches

## Start new work
- `git switch main`
- `git pull --ff-only`

## Stage and commit
- `git add -p path/to/file`  # stage specific hunks
- `git commit -m "<msg-type: title>"`
- `git commit --amend` # fix last commit (messages/files)
- `git commit --amend --no-edit` # fix last commit (messages)

## Publish & branch
- `git push -u origin my-branch`
- `git pull --ff-only` 
# if diverged
- `git fetch origin`
- `git reset --hard origin/main`

## Compare & inspect changes
- `git diff`    # unstaged changes
- `git diff --staged` # what will be committed
- `git show HEAD` # last commit (diff & meta)
- `git log -p path/to/file`
- `git blame path/to/file`

## Undo safely (published history)
- `git revert <commit>` # make a new commit that undoes <commit>

## Reset (local rewrite; careful)
# Reset moves branch/HEAD to <commit>
                                #Staging Area/Working Tree (files)
- `git reset --soft <commit>`   #Keeps/Keeps
- `git reset --mixed <commit>`  #Unstages changes/Keeps
- `git reset --hard <commit>`   #Resets to <commit>/Resets to <commit>
- `git clean -fd`   # remove untracked files/dirs (dangerous)

## Keep branch current (rebasing)
- `git fetch origin`
- `git rebase origin/main`
# Tidy last N commits (squash/reword)
- `git rebase -i HEAD~5`
- `git rebase --continue | --abort`

## Bring specific commits (surgical)
- `git cherry-pick <sha1> [<sha2> ...]
- `git cherry-pick --abort`

## Stash WIP
- `git stash push -m "wip: note"`
- `git stash list`
- `git stash pop` # apply + drop
- `git stash apply` # apply, keep in stash

## Branch housekeeping
- `git branch -m old new` # rename current branch
- `git branch -d name` # delete merged local branch
- `git branch -D name` # force delete local branch
- `git push origin :name` # delete remote branch
- `git fetch --all --prune` # update remotes, drop deleted refs
- `git push origin --delete <branch-name>` # deletes branch on remote

## Remotes
- `git remote add origin https://...git`
- `git remote set-url origin https://...git`
- `git push -u origin main` # first push sets upstream

## Rescue (when things go sideways)
- `git reflog`  # find a good SHA
- `git checkout -b rescue <sha>` # recover work to a new branch
- `git restore source=<sha> --path/to/file` # get on file from a past commit

## Tags (releases)


# Other commands to know
## Inspect & status
- `git rev-parse --abbrev-ref HEAD` # gives branch where HEAD is pointed

## History & search
- `git log --oneline --decorate --graph --all`  # this is pretty unclear to me
- `git log -S "string"`                         # search code changes containing string"

## Diff & stage
- `git restore <path>`          # discard working-tree changes to a file
- `git restore --staged <path>` # unstage a file

## Undo & fix (safe-first)
- `git restore <path>`  # discard working-tree changes to file
- `git revert <commit>` # make a new commit that undoes <commit> (reverts are safest for published history)
