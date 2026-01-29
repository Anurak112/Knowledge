---
name: git-commit-helper
description: Generate descriptive commit messages. ช่วยสร้างข้อความ commit จากการวิเคราะห์ git diff
version: 1.0.0
---

# Git Commit Helper

## Quick start

Analyze staged changes and generate commit message:

```bash
# View staged changes
git diff --staged

# Generate commit message based on changes
# (Claude will analyze the diff and suggest a message)
```

## Commit message format

Follow conventional commits format:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, missing semicolons)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

## Interactive commit helper

Use `git add -p` for selective staging:

```bash
# Stage changes interactively
git add -p

# Review what's staged
git diff --staged

# Commit with message
git commit -m "type(scope): description"
```
