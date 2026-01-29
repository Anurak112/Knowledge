# MCP (Model Context Protocol)

This directory contains configurations for MCP servers, which extend the agent's capabilities by providing access to external tools and resources.

## Structure

```
mcps/
├── servers/
│   └── server-config.json  # Configuration for a specific MCP server
└── resources/
    └── ...                 # Additional resources for MCPs
```

## Format

MCP server configurations are JSON files defining how to launch the server.

```json
{
  "name": "server-name",
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-name"],
  "env": {
    "API_KEY": "..."
  }
}
```
