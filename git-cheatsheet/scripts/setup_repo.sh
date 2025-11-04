#!/bin/bash

# This script sets up a new Git repository with a basic structure.

# Check if a directory name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <repository-name>"
    exit 1
fi

REPO_NAME=$1

# Create the repository directory
mkdir "$REPO_NAME"
cd "$REPO_NAME" || exit

# Initialize a new Git repository
git init

# Create basic directory structure
mkdir -p docs exercises/python exercises/bash examples/simple-app/src tests scripts

# Create placeholder files
touch docs/cheat_sheet.md docs/commands.md docs/workflows.md
touch exercises/python/bubble_sort.py exercises/bash/commit_practice.sh exercises/review_checklist.md
touch tutorials/getting-started.md tutorials/branching-and-merging.md
touch examples/simple-app/src/main.py examples/simple-app/README.md
touch tests/test_bubble_sort.py

# Create .gitignore, CONTRIBUTING.md, LICENSE, and README.md
touch .gitignore CONTRIBUTING.md LICENSE README.md

echo "Git repository '$REPO_NAME' has been set up with a basic structure."