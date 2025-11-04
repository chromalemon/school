# Git Commands Cheat Sheet

## Basic Commands

### git init
- **Description**: Initializes a new Git repository.
- **Usage**: `git init [repository-name]`
- **Example**: `git init my-repo`

### git clone
- **Description**: Creates a copy of an existing repository.
- **Usage**: `git clone [url]`
- **Example**: `git clone https://github.com/user/repo.git`

### git add
- **Description**: Stages changes for the next commit.
- **Usage**: `git add [file]` or `git add .` (to add all changes)
- **Example**: `git add index.html`

### git commit
- **Description**: Records the staged changes in the repository.
- **Usage**: `git commit -m "commit message"`
- **Example**: `git commit -m "Add new feature"`

### git status
- **Description**: Displays the state of the working directory and staging area.
- **Usage**: `git status`
- **Example**: `git status`

### git push
- **Description**: Uploads local repository content to a remote repository.
- **Usage**: `git push [remote] [branch]`
- **Example**: `git push origin main`

### git pull
- **Description**: Fetches and integrates changes from a remote repository.
- **Usage**: `git pull [remote] [branch]`
- **Example**: `git pull origin main`

## Branching Commands

### git branch
- **Description**: Lists, creates, or deletes branches.
- **Usage**: `git branch [branch-name]`
- **Example**: `git branch feature-branch`

### git checkout
- **Description**: Switches to a specified branch or restores working tree files.
- **Usage**: `git checkout [branch-name]`
- **Example**: `git checkout feature-branch`

### git merge
- **Description**: Combines changes from one branch into another.
- **Usage**: `git merge [branch-name]`
- **Example**: `git merge feature-branch`

## Remote Commands

### git remote
- **Description**: Manages set of tracked repositories.
- **Usage**: `git remote [add|remove|rename] [name] [url]`
- **Example**: `git remote add origin https://github.com/user/repo.git`

### git fetch
- **Description**: Downloads objects and refs from another repository.
- **Usage**: `git fetch [remote]`
- **Example**: `git fetch origin`

## Viewing History

### git log
- **Description**: Shows the commit history for the current branch.
- **Usage**: `git log`
- **Example**: `git log --oneline`

### git diff
- **Description**: Shows changes between commits, commit and working tree, etc.
- **Usage**: `git diff [options]`
- **Example**: `git diff HEAD`

## Stashing Changes

### git stash
- **Description**: Stashes changes in a dirty working directory.
- **Usage**: `git stash`
- **Example**: `git stash save "work in progress"`

### git stash pop
- **Description**: Applies the changes stashed away and removes them from the stash list.
- **Usage**: `git stash pop`
- **Example**: `git stash pop`

## Conclusion
This cheat sheet provides a quick reference to essential Git commands. For more detailed explanations and advanced usage, refer to the official Git documentation or the other files in this project.