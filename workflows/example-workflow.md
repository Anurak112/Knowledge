---
description: Example workflow for code review
tags: [dev, review]
---

# Code Review Workflow

1.  **Check Out Branch**: Ensure you are on the correct branch to be reviewed.
2.  **Analyze Diff**: Run `git diff main...HEAD` to see changes.
3.  **Review Logic**:
    -   Check for potential bugs.
    -   Verify error handling.
4.  **Review Style**:
    -   Ensure consistent indentation.
    -   Check variable naming conventions.
5.  **Run Tests**: Execute the test suite and verify all pass.
6.  **Submit Feedback**: Summarize findings in the pull request comments.
