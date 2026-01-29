# Skills

Skills are specialized capabilities that an agent can "learn" and execute. A skill is a package containing instructions, scripts, and resources.

## Structure

```
skills/
└── skill-name/
    ├── SKILL.md          # REQUIRED: Main instruction file
    ├── scripts/          # Helper scripts
    ├── examples/         # Usage examples
    └── resources/        # Additional files/templates
```

## SKILL.md Format

The `SKILL.md` file must contain YAML frontmatter followed by markdown instructions.

```markdown
---
name: skill-name
description: A short description of what this skill does
version: 1.0
---

# Instructions

Detailed step-by-step instructions on how the agent should perform this skill.
```
