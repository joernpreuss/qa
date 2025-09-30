# QA - Quality Assurance Tooling

An interactive QA tool for Python projects featuring parallel testing, database switching, and a rich terminal interface.

## Project Status

**Phase: Planning & Analysis**

This repository documents the extraction of a QA tool from another project. The analysis phase demonstrates systematic project planning, dependency mapping, and migration strategy development.

## Project Overview

This project extracts and generalizes a custom QA tool originally built for internal use, transforming it into a standalone, reusable developer tool. The tool provides:

- **Interactive Menu System** - Single-key navigation for common QA tasks
- **Parallel Test Execution** - Configurable worker pools (Fibonacci sequence selection)
- **Database Switching** - Seamless SQLite/PostgreSQL test environment toggling
- **Rich Terminal Output** - Color-coded output with progress indicators
- **Unified Formatting** - Coordinated code (Ruff) and template (djlint) formatting
- **Smart Integration** - Project-specific configuration via `pyproject.toml`

## Documentation

Planning documents available in [`docs/planning/`](docs/planning/):

- **[CLI Commands Analysis](docs/planning/2025-09-25-cli-commands.md)** - Complete command structure and user interaction flows
- **[Configuration Schema](docs/planning/2025-09-25-config-schema.md)** - PyPI-ready configuration design with validation
- **[Integration Analysis](docs/planning/2025-09-25-integration-analysis.md)** - Current usage patterns, dependencies, and migration strategy
- **[References Analysis](docs/planning/2025-09-25-references-analysis.md)** - Full dependency mapping and impact assessment

## Key Features (Planned)

### Interactive Workflows
```bash
qa i              # Interactive menu with rerun options
qa check          # Run all QA checks with results summary
qa check --fix    # Auto-fix all issues
```

### Individual Commands
```bash
qa format         # Code + template formatting
qa lint           # Linting checks
qa typecheck      # Type checking with mypy
qa test           # Run test suite
qa newlines       # Trailing newlines validation
```

### Configuration Example
```toml
[tool.qa]
lint_tool = ["ruff", "check"]
format_tool = ["ruff", "format"]
typecheck_tool = ["mypy"]
paths = ["src/", "tests/"]
template_paths = ["templates/"]
```

## Technical Approach

### Analysis Methodology
- Codebase scanning for dependencies and references
- Integration point mapping with CI/CD systems
- Migration impact assessment across documentation and workflows
- Backwards compatibility planning

### Architecture Decisions
- **Tool Execution**: `uv tool run` for isolated environments
- **Configuration**: `pyproject.toml` with `[tool.qa]` section
- **Extensibility**: Plugin architecture for custom checks
- **Distribution**: PyPI package with global installation

## Development Timeline

- ✅ **Phase 0: Analysis** (Current) - Requirements gathering and documentation
- 🔄 **Phase 1: Extraction** - Code isolation and generalization
- 📋 **Phase 2: Testing** - Test coverage and validation
- 📋 **Phase 3: Distribution** - PyPI packaging and documentation
- 📋 **Phase 4: Migration** - Original project integration

## Technology Stack

- **CLI Framework**: Typer with Rich for terminal UI
- **Testing**: pytest with xdist for parallelization
- **Type Checking**: mypy with strict configuration
- **Code Quality**: Ruff for linting and formatting
- **Template Support**: djlint for Jinja2/HTML templates
- **Package Management**: uv for modern Python tooling

## Installation (Future)

Once published to PyPI:

```bash
uv tool install qa
```

## License

MIT License - See [LICENSE](LICENSE) for details

## Author

Jörn Preuß ([joern.preuss@gmail.com](mailto:joern.preuss@gmail.com))
