# qa

Sophisticated QA tooling with interactive menus, parallel testing, and database switching.

## Installation

```bash
uv tool install qa
```

## Usage

```bash
# Interactive mode
qa i

# Check all QA aspects
qa check

# Format code
qa format

# Run linting
qa lint

# Type checking
qa typecheck
```

## Features

- Interactive menu system with single-key navigation
- Parallel test execution with configurable workers
- Database switching (SQLite/PostgreSQL)
- Rich terminal output with colors and emojis
- Project-specific configuration via `pyproject.toml`

## Configuration

Add to your `pyproject.toml`:

```toml
[tool.qa]
lint_tool = ["ruff", "check"]
format_tool = ["ruff", "format"]
paths = ["src/", "tests/"]
```

## Development Status

🚧 **In Development** - Extracted from another project, currently in Phase 0 of the export plan.

## License

MIT