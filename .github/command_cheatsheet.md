
--- # WORKFLOW FOR SOLO PROJECTS --- 
# start work on new feature
`git switch -c <new-branch>`

# checkpoint often
`git add .`
`git commit -m "wip: <what you did>"`

# when done with significant part of task or step away - push to GH
`git push -u origin <new-branch>` or `git push`

# when fully done with task: push => sanity check
`git add .; git commit -m "feat/fix/chore: <describe whole task>"`
`git log --oneline --decorate --graph --all` # sanity check
`git push`

# open and merge a PR
`gh pr create --title "feat: <task> --body "short summary" --base main --head <new-branch>` # creates PR from head to base 
`gh pr merge --squash --delete-branch` # merge open PR combine all commits into 1 with title & body taken from PR

# finish (squash & clean-up)
`git switch main`
`git pull --ff-only` # ff-only is a safety mechanism - ensures that there are no commits on local that aren't on remote
`git fetch --prune` # keeps origin/ * tidy locally 

--- # CREATE A REMOTE REPO & CONNECT ---
## Create repo
`gh repo create <repo-name> --public`
## Connect
`git remote add origin https://github.com/elikent/<repo-name>.git`


--- # EXPLORE ---
- `git status` # shows changes in working tree not added to staging area and changes staged but not committed
- `git fetch origin`  # downloads current state of origin
- `git log oneline main..origin/main` # shows if remote is ahead
- `git log oneline origin/main..main` # shows if local is ahead
- `git show <commit-hash>` # get commit header and diff
- `git show HEAD` # get commit header and diff for HEAD
- `git show --no-patch <commit-hash>` # get metadata only
- `git show --name-only <commit-hash>` # metadata + file names
- `git remote -v` # (gives origin for fetch and push)
- Note: `git switch -c tmp origin/some/branch` will 

--- # NAVIGATE ---
# Navigate to last branch i was on
- `git switch -`

--- # IF MAIN AND ORIGIN/MAIN DIVERGE---
# Stash local changes
- `git stash push -m "WIP before syncing main"`
# Reset main to origin/main
- `git switch main`
- `git fetch origin`
- `git reset --hard origin/main`
# Create new branch, pop stash, save => add => commit
- `git switch -c <branch-name>`
- `git pip stash{0}`
- save file(s)
- `git add .`
- `git commmit ...`
# Publish and PR
- `git push -u origin <branch-name>`
- `gh pr create .....`
- `gh pr merge --squash --delete-branch`
# Update local and tidy
- `git switch main`
- `git pull --ff-only`
- `git fetch --prune`

--- # WORKFLOW FOR COLLAB PROJECTS ---
# start work on new feature
`git switch -c <new-branch>`

# checkpoint often
`git add .`
`git commit -m "wip: <what you did>"`

# when done with significant part of task or step away - push to GH
`git push -u origin <new-branch>`

# when fully done with task: push => sanity check
`git add .; git commit -m "feat/fix/chore: <describe whole task>"`
`git push`
`git log --oneline --decorate --graph --all`

# rebase to latest main
`git fetch origin`
`git rebase origin/main`  
`git push --force-with-lease`

# open and merge a PR
`gh pr create --title "feat: <task> --body "short summary" --base main --head <new-branch>` # creates PR from head to base 
`gh pr merge --squash --delete-branch` # merge open PR combine all commits into 1 with title & body taken from PR

# finish (squash & clean-up)
`git switch main`
`git pull --ff-only` # ff-only is a safety mechanism - ensures that there are no commits on local that aren't on remote
`git fetch --prune` # keeps origin/ * tidy locally 



--- # IF WORKED ON MAIN BY ACCIDENT ---
# Move local commit(s) off main 
- `git switch -c chore/move-off-main`

# Reset local to match remote 
- `git switch main`
- `git fetch origin`
- `git reset --hard origin/main`

# PR the branch back into main
- `git switch chore/move-off-main` 
- `gh pr create --fill --base main --head chore/move-off-main`
- `gh pr merge --squash --delete-branch`

# Sync local main
- `git switch main`
- `git pull --ff-only`
- `git fetch --prune` # keeps origin/ * tidy locally 

---

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
