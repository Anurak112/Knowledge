# Code Quality Context / Context ที่เน้นเรื่องคุณภาพโค้ด

## Metrics
- **Cyclomatic Complexity**: Keep under 10.
- **Function Length**: Max 20 lines preferred.
- **Duplication**: 0% tolerance for logic duplication.

## Tools
- ESLint / Pylint
- Prettier / Black
- SonarQube

## Procedures
- Run linting before every commit.
- Address all warnings, treat them as errors.
- Refactor legacy code when touching it (Boy Scout Rule).
