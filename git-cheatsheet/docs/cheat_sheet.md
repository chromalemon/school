# Git Cheat Sheet

## Basic Commands

- **git init**: Initializes a new Git repository.
- **git clone [url]**: Clones an existing repository from a remote URL.
- **git add [file]**: Stages changes in the specified file for the next commit.
- **git commit -m "[message]"**: Commits the staged changes with a descriptive message.
- **git status**: Displays the status of the working directory and staging area.
- **git log**: Shows the commit history for the current branch.
- **git diff**: Displays changes between commits, commit and working tree, etc.

## Branching

- **git branch**: Lists all local branches in the repository.
- **git branch [branch-name]**: Creates a new branch.
- **git checkout [branch-name]**: Switches to the specified branch.
- **git merge [branch-name]**: Merges the specified branch into the current branch.
- **git rebase [branch-name]**: Reapplies commits on top of another base tip.

## Remote Repositories

- **git remote -v**: Lists all remote repositories.
- **git fetch [remote]**: Fetches changes from the remote repository without merging.
- **git pull [remote] [branch]**: Fetches and merges changes from the remote branch into the current branch.
- **git push [remote] [branch]**: Pushes local changes to the specified remote branch.

## Undoing Changes

- **git reset [file]**: Unstages the specified file.
- **git checkout -- [file]**: Discards changes in the working directory.
- **git revert [commit]**: Creates a new commit that undoes the changes made in the specified commit.

## Stashing

- **git stash**: Stashes the changes in the working directory.
- **git stash apply**: Applies the stashed changes back to the working directory.
- **git stash pop**: Applies the stashed changes and removes them from the stash.

## Tags

- **git tag**: Lists all tags in the repository.
- **git tag [tag-name]**: Creates a new tag.
- **git push [remote] [tag-name]**: Pushes the specified tag to the remote repository.

## Configuration

- **git config --global user.name "[name]"**: Sets the name for commits.
- **git config --global user.email "[email]"**: Sets the email for commits.
- **git config --list**: Lists all Git configuration settings.

## Best Practices

- Commit often with clear messages.
- Use branches for new features or bug fixes.
- Regularly pull changes from the remote repository.
- Review changes before merging.