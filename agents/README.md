# Agents

This directory contains configuration files for Agents and Subagents.

-   **`agents/`**: Top-level agent configurations.
-   **`subagents/`**: Specialized sub-agent configurations called by top-level agents.

## Format

Agent configurations are typically YAML files defining the model, system prompt, and available tools.

```yaml
name: Agent Name
description: Purpose of the agent
model: gemini-2.0-flash
system_prompt: path/to/prompt/file.md OR inline string
tools:
  - tool_name_1
  - tool_name_2
subagents:
  - subagent_name
```
