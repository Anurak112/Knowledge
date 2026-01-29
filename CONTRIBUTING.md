# Contributing to the Knowledge Repository

Thank you for your interest in contributing! This repository relies on structured, consistent data to empower AI agents. Following these guidelines ensures that all agents can correctly parse and utilize the knowledge, skills, and tools stored here.

## General Guidelines

1.  **Follow the Structure**: Place files in their appropriate directories (e.g., new skills go in `skills/`).
2.  **Use Documentation**: Every major component (skill, workflow, agent) should have self-contained documentation or comments.
3.  **Stick to Formats**: Use the established file formats (YAML for configs, Markdown for docs/prompts, JSON for strict schemas) as defined in each directory's README.

## Adding a New Skill

1.  Create a new folder in `skills/` named after your skill (kebab-case, e.g., `web-scraping`).
2.  Create a `SKILL.md` file inside that folder. Follow the template in `skills/README.md`.
3.  Add any necessary scripts to `scripts/` and examples to `examples/` within your skill folder.

## Adding a Workflow

1.  Create a new Markdown file in `workflows/` (e.g., `deploy-to-prod.md`).
2.  Use the YAML frontmatter to define metadata (description, tags).
3.  List clear, step-by-step instructions.

## Adding configurations (Agents, MCPs, Settings)

1.  Refer to the specific directory's README for the required schema.
2.  Validate your YAML/JSON before committing to ensure no syntax errors break the agent's loading process.

## Pull Requests

-   Describe clearly what your change adds or fixes.
-   If you are adding a new complex capability, include a small usage example or test case.

Thank you for building a smarter future!
