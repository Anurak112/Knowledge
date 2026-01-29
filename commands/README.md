# Commands

This directory defines custom commands that can be executed by the agent. These can be shell commands, scripts, or complex tool invocations alias.

## Format

```yaml
name: command-name
description: What the command does
command: The actual shell command to run
cwd: Optional working directory
safe_to_auto_run: boolean
```
