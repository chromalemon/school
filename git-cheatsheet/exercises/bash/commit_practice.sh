#!/bin/bash

# This script is designed to help you practice making commits in Git.

# Create a new directory for the practice repository
mkdir git-practice
cd git-practice

# Initialize a new Git repository
git init

# Create a sample file to commit
echo "This is a practice file for Git commit." > practice.txt

# Stage the file for commit
git add practice.txt

# Commit the changes
git commit -m "Initial commit: Add practice file"

# Prompt the user to make changes
echo "Now, modify the practice.txt file and save your changes."
read -p "Press enter to continue after making changes..."

# Stage the modified file
git add practice.txt

# Commit the changes
git commit -m "Update practice file with new content"

# Display the commit history
echo "Here is your commit history:"
git log --oneline

# End of script
echo "Practice complete! You can explore your commits using 'git log'."