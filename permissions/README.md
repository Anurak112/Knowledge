# Permissions

This directory controls access to tools and resources through Role-Based Access Control (RBAC).

## Categories

-   **`roles/`**: Definitions of roles (e.g., Admin, Viewer, Editor).
-   **`policies/`**: Specific rules granting or denying access.

## Format

Permissions are often defined in YAML.

```yaml
role: output_only
allowed_commands:
  - echo
  - ls
denied_commands:
  - rm
  - write_to_file
```
