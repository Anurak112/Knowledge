---
name: find-skills
description: Discover and install skills for AI agents using the Skills CLI.
version: 1.0.0
---

# Overview

This skill helps you discover and install skills from the open agent skills ecosystem using the `npx skills` command.

# Instructions

## Step 1: Understand What They Need
When a user asks for help with something, identify:
1.  The domain (e.g., React, testing, design, deployment)
2.  The specific task (e.g., writing tests, creating animations, reviewing PRs)
3.  Whether this is a common enough task that a skill likely exists

## Step 2: Search for Skills
Run the find command with a relevant query:

```bash
npx skills find [query]
```

**Examples:**
-   "how do I make my React app faster?" -> `npx skills find react performance`
-   "can you help me with PR reviews?" -> `npx skills find pr review`
-   "I need to create a changelog" -> `npx skills find changelog`

## Step 3: Present Options to the User
When you find relevant skills, present them to the user with:
1.  The skill name and what it does
2.  The install command they can run
3.  A link to learn more at skills.sh

**Example Response:**
> I found a skill that might help! The "vercel-react-best-practices" skill provides React and Next.js performance optimization guidelines from Vercel Engineering.
> To install it: `npx skills add vercel-labs/agent-skills@vercel-react-best-practices`
> Learn more: https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices

## Step 4: Offer to Install
If the user wants to proceed, you can install the skill for them:

```bash
npx skills add <owner/repo@skill> -g -y
```

-   `-g` installs globally (user-level)
-   `-y` skips confirmation prompts

## When No Skills Are Found
If no relevant skills exist:
1.  Acknowledge that no existing skill was found.
2.  Offer to help with the task directly using your general capabilities.
3.  Suggest the user could create their own skill with `npx skills init`.

# Tips for Effective Searches
1.  Use specific keywords: "react testing" is better than just "testing"
2.  Try alternative terms: If "deploy" doesn't work, try "deployment" or "ci-cd"
