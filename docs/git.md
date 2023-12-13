# Git

Welcome to the Git User Guide! In this guide, we'll walk you through common Git operations, including installation, uninstallation, basic commands, branch management, committing, fetching, pulling, pushing, creating a merge request in GitLab, and merging branches.

## Table of Contents
- [Git](#git)
  - [Table of Contents](#table-of-contents)
  - [What is Git ? And why we use it ?](#what-is-git--and-why-we-use-it-)
  - [Disclamer](#disclamer)
  - [Installation](#installation)
  - [Installation via Package Manager](#installation-via-package-manager)
  - [Uninstall](#uninstall)
  - [Basic Git Commands](#basic-git-commands)
    - [Add](#add)
    - [Commit](#commit)
    - [Status](#status)
    - [Log](#log)
  - [Branch Management](#branch-management)
    - [Create and Switch Branches](#create-and-switch-branches)
    - [Squash Commits](#squash-commits)
  - [Remote Repository Interaction](#remote-repository-interaction)
    - [Fetch](#fetch)
    - [Pull](#pull)
    - [Push](#push)
    - [Create a Merge Request in GitLab](#create-a-merge-request-in-gitlab)
    - [Merge Two Branches](#merge-two-branches)

## What is Git ? And why we use it ?

Git is a distributed version control system (DVCS) that is widely used in software development and other fields to track and manage changes to source code and other files. It was created by Linus Torvalds in 2005 and has since become ~~one of~~ **the most** popular version control systems in the world. Here are some key concepts and features of Git:

1. **Version Control**: Git allows you to track changes to your project's files over time. It records a history of all modifications, who made them, and when they were made.

2. **Distributed**: Git is a distributed version control system, which means that every developer working on a project has a full copy of the entire repository, including its history. This enables developers to work independently, even when they are not connected to a central server.

3. **Branching and Merging**: Git makes it easy to create branches, which are separate lines of development. Developers can work on features or bug fixes in their own branches and then merge their changes back into the main branch when they are ready.

4. **Collaboration**: Git facilitates collaboration among developers. Multiple people can work on the same project simultaneously, and Git helps manage conflicts when multiple changes overlap.

5. **Remote Repositories**: Git supports remote repositories, allowing teams to work together on a project, even when team members are in different locations. Popular hosting services like GitHub, GitLab, and Bitbucket provide a platform for hosting Git repositories in the cloud.

6. **Commit History**: Git maintains a detailed commit history that includes information about each change, such as the author, date, and a commit message explaining the purpose of the change.

7. **Revert and Rollback**: Git allows you to easily revert to previous versions of your project if a mistake is made or if you need to go back to an earlier state.

8. **Security and Integrity**: Git uses cryptographic hashes to ensure the integrity of your project's history. This means that once data is committed to a Git repository, it cannot be changed without leaving a trace.

9. **Open Source**: Git is open source software and is available for free. It has a large and active community of users and contributors who continue to improve and extend its functionality.

Git is an essential tool for software development but is also used in various other domains where version control and change tracking are important, such as documentation, configuration management, and more. Learning how to use Git effectively is a valuable skill for anyone involved in collaborative or versioned work.

## Disclamer

If you prefer not to use git in the terminal or if you don't feel confidant enough to using the terminal, we **higly recommend** using `sublime-merge`. It offers a user interface for git, that make it easier to understand and use all the git commands.

## Installation

If you haven't already installed Git, follow these steps:

1. Download Git for your specific platform from [https://git-scm.com/downloads](https://git-scm.com/downloads).

2. Run the installer and follow the installation instructions.

3. To verify that Git is installed, open your terminal/command prompt and run:

   ```bash
   git --version
   ```

   You should see the Git version you installed.

## Installation via Package Manager

On Debian-based distributions like Ubuntu, you can use the `apt` package manager to install Git:

```bash
sudo apt update
sudo apt install git
```


## Uninstall

If you ever need to uninstall Git, follow these steps based on your platform:

- **Windows:**

  Use the "Add or Remove Programs" feature in the Control Panel to uninstall Git.

- **macOS:**

  You can uninstall Git using Homebrew by running:

  ```bash
  brew uninstall git
  ```

- **Linux:**

  Use your system's package manager to uninstall Git. For example, on Ubuntu:

  ```bash
  sudo apt-get remove git
  ```

## Basic Git Commands

### Add

Git allows you to selectively choose which changes you want to include in the next commit. This process is called "staging." You use the git add command to stage changes.

```bash
git add filename
```

### Commit

A "commit" refers to a fundamental operation that records changes to a set of files in a repository. When you make changes to files within a Git repository. Commits are the building blocks of a Git repository's history. They allow you to track changes over time, collaborate with others, and easily revert to previous states of your project if needed.

To save your changes to the repository, use the following command:

```bash
git commit -m "Your commit message"
```

This command commits your changes to the current branch with a descriptive message.

### Status

To check the status of your working directory, including untracked and modified files, use:

```bash
git status
```

This command helps you keep track of changes in your repository.

### Log

To view the commit history, use:

```bash
git log
```

This command displays a list of commits, including their messages and authors.

## Branch Management

### Create and Switch Branches

Branches in Git provide a powerful way to organize and manage development efforts, enabling parallel work, experimentation, code review, and the ability to address issues and features in an organized and controlled manner. They help maintain code stability and facilitate efficient collaboration among developers.

To create a new branch and switch to it, use:

```bash
git checkout -b new-branch-name
```

This command creates a new branch and switches to it.
Alternativelly, if you wish to just create a new branch, use:

```bash
git branch new-branch-name
```

### Squash Commits

To combine multiple commits into a single commit, use an interactive rebase:

```bash
git rebase -i HEAD~n
```

Replace `n` with the number of commits you want to squash. Follow the interactive rebase instructions to squash the commits.

## Remote Repository Interaction

### Fetch

To update your local repository with changes from the remote repository, use:

```bash
git fetch
```

This command fetches changes without automatically merging them into your local branch.

### Pull

To fetch and merge changes from the remote repository into your current branch, use:

```bash
git pull
```

This command updates your local branch with remote changes.

### Push

To push your local changes to the remote repository, use:

```bash
git push
```

This command uploads your local commits to the remote repository.

### Create a Merge Request in GitLab

1. Go to your GitLab repository on the GitLab website.

2. Click on the "Merge Requests" tab.

3. Click the "New Merge Request" button.

4. Select the source branch and target branch for the merge request.

5. Add a title and description for your merge request.

6. Click the "Submit merge request" button.

### Merge Two Branches

To merge two branches (e.g., feature-branch into main), you can use the following steps:

1. Checkout the target branch (e.g., main):

   ```bash
   git checkout main
   ```

2. Merge the source branch (e.g., feature-branch) into the target branch:

   ```bash
   git merge feature-branch
   ```

3. Resolve any merge conflicts if they occur.

4. Commit the merge:

   ```bash
   git commit -m "Merge feature-branch into main"
   ```

5. Push the changes to the remote repository:

   ```bash
   git push
   ```

That's it! You're now equipped with essential Git commands and GitLab operations to manage your Git repositories. Happy coding and collaborating!