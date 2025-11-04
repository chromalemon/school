# filepath: /git-cheatsheet/git-cheatsheet/tutorials/getting-started.md
# Getting Started with Git

## Introduction
Git is a distributed version control system that allows multiple developers to work on a project simultaneously without interfering with each other's changes. It tracks changes in source code during software development, enabling collaboration and version management.

## Installation
To get started with Git, you need to install it on your machine. Follow the instructions below based on your operating system:

### For Ubuntu
1. Open your terminal.
2. Update your package index:
   ```
   sudo apt update
   ```
3. Install Git:
   ```
   sudo apt install git
   ```

### For macOS
1. Open your terminal.
2. Install Git using Homebrew:
   ```
   brew install git
   ```

### For Windows
1. Download the Git installer from [git-scm.com](https://git-scm.com/download/win).
2. Run the installer and follow the setup instructions.

## Initial Setup
After installing Git, you need to configure your user information. This is important for tracking who makes changes to the repository.

1. Set your username:
   ```
   git config --global user.name "Your Name"
   ```
2. Set your email address:
   ```
   git config --global user.email "your.email@example.com"
   ```

## Creating a New Repository
To create a new Git repository, follow these steps:

1. Navigate to your project directory:
   ```
   cd path/to/your/project
   ```
2. Initialize a new Git repository:
   ```
   git init
   ```

## Basic Git Commands
Here are some essential Git commands to get you started:

- **Check the status of your repository:**
  ```
  git status
  ```

- **Add changes to the staging area:**
  ```
  git add <file>
  ```

- **Commit changes:**
  ```
  git commit -m "Your commit message"
  ```

- **View commit history:**
  ```
  git log
  ```

## Conclusion
This guide provides a basic overview of getting started with Git. For more advanced topics, such as branching and merging, refer to the other tutorials in this project. Happy coding!