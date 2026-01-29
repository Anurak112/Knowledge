# Modes

Modes define different operational states for the agent, tailored for specific phases of development (e.g., Planning, Coding, Debugging).

## Format

Mode definitions typically specify which tools are available and how the system prompt should be adjusted.

```yaml
name: Planning
description: For architectural design and requirement gathering
allowed_tools:
  - read_file
  - search_web
system_prompt_addendum: "Focus on high-level design and avoid writing implementation code."
```
