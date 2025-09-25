# QA Tool Configuration Schema

Based on the source project's current implementation (noxfile.py + qa.py analysis).

## Configuration Discovery Priority

1. `pyproject.toml [tool.qa]` section (primary)
2. `qa.toml` dedicated file (fallback)
3. `noxfile.py` function imports (backwards compatibility)
4. Default values (sensible generic configuration)

## Core Configuration Schema

```toml
[tool.qa]
# Tool configurations (from source project noxfile.py)
lint_tool = ["uv", "tool", "run", "ruff", "check"]
lint_paths = ["src/", "tests/"]

format_tool = ["uv", "tool", "run", "ruff", "format"]
format_paths = ["src/", "tests/"]

typecheck_tool = ["uv", "tool", "run", "mypy"]
typecheck_paths = ["src/", "tests/"]

# Template support (source project has templates/)
has_templates = true
template_tool = ["uv", "run", "djlint"]
template_paths = ["templates/"]

# Test execution
test_tool = ["uv", "run", "pytest"]
test_paths = ["tests/"]
test_args = ["--color=yes"]

# Custom script integration
newlines_script = "src/tools/check_newlines.py"  # source project-specific
requirements_tool = ["uv", "run", "pytreqt", "show"]  # source project-specific

# Interactive features (Fibonacci sequence from qa.py:536)
parallel_workers = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 120, 160, 200]
default_database = "sqlite"

# Database testing (source project-specific)
databases = ["sqlite", "postgresql"]
sqlite_url = "sqlite:///./test.db"
postgresql_url = "postgresql://savt_user:savt_password@localhost:5432/savt"
test_env_var = "TEST_DATABASE"
test_database_env = "DATABASE_URL"

# Tool execution
runner = "uv"  # or "python", "pipx", etc.
```

## Default Values (Generic Python Project)

```toml
[tool.qa]
# Minimal generic configuration
lint_tool = ["ruff", "check"]
format_tool = ["ruff", "format"]
typecheck_tool = ["mypy"]
test_tool = ["pytest"]

# Standard paths
lint_paths = ["src/", "tests/"]
format_paths = ["src/", "tests/"]
typecheck_paths = ["src/", "tests/"]
test_paths = ["tests/"]

# Interactive defaults
parallel_workers = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 120, 160, 200]
has_templates = false
databases = ["sqlite"]
```

## source project Migration Configuration

This preserves exact current source project behavior:

```toml
[tool.qa]
# Exact source project tool commands (from noxfile.py)
lint_tool = ["uv", "tool", "run", "ruff", "check"]
lint_paths = ["src/", "tests/"]
format_tool = ["uv", "tool", "run", "ruff", "format"]
format_paths = ["src/", "tests/"]
typecheck_tool = ["uv", "tool", "run", "mypy"]
typecheck_paths = ["src/", "tests/"]

# source project template support
has_templates = true
template_tool = ["uv", "run", "djlint"]
template_paths = ["templates/"]

# source project database testing
databases = ["sqlite", "postgresql"]
postgresql_url = "postgresql://savt_user:savt_password@localhost:5432/savt"
test_env_var = "TEST_DATABASE"

# source project custom integrations
newlines_script = "src/tools/check_newlines.py"
requirements_tool = ["uv", "run", "pytreqt", "show"]

# Interactive features (preserve Fibonacci sequence)
parallel_workers = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 120, 160, 200]
default_database = "sqlite"

runner = "uv"
```

## Configuration Loading Logic

```python
def load_config(start_path: Path = None) -> QAConfig:
    """Load configuration with discovery priority."""
    start_path = start_path or Path.cwd()

    # Walk up directory tree like nox does
    for path in [start_path] + list(start_path.parents):
        # 1. Check pyproject.toml [tool.qa]
        pyproject = path / "pyproject.toml"
        if pyproject.exists():
            config = load_from_pyproject(pyproject)
            if config:
                return config

        # 2. Check qa.toml
        qa_toml = path / "qa.toml"
        if qa_toml.exists():
            return load_from_toml(qa_toml)

        # 3. Check noxfile.py (backwards compatibility)
        noxfile = path / "noxfile.py"
        if noxfile.exists():
            config = load_from_noxfile(noxfile)
            if config:
                return config

    # 4. Return defaults
    return DEFAULT_CONFIG
```

## Abstraction Strategy

### Hardcoded → Configurable

**Current source project hardcoded values** → **Configuration keys**:
- `["src/", "tests/"]` → `lint_paths`, `format_paths`, `typecheck_paths`
- `"uv tool run ruff check"` → `lint_tool`
- `"DATABASE_URL=postgresql://..."` → `postgresql_url`
- `"templates/"` → `template_paths`
- Fibonacci workers → `parallel_workers`

### Backwards Compatibility

Support importing from `noxfile.py`:
```python
try:
    from noxfile import get_lint_command, get_format_command, get_typecheck_command
    # Use noxfile functions
except ImportError:
    # Use configuration file
```

## Benefits

✅ **100% source project feature parity** - All current functionality preserved
✅ **Project flexibility** - Any Python project structure supported
✅ **Gradual adoption** - Backwards compatible with noxfile.py
✅ **Modern standards** - Following pytreqt/nox configuration patterns