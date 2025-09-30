# SAVT Integration Analysis

Current usage patterns and integration points for qa tool extraction.

## Current Usage Patterns

### 1. Entry Point Configuration

**pyproject.toml**: Direct script entry point
```toml
[project.scripts]
qa = "src.tools.qa.qa:main"
```

### 2. Installation Method

**Command**: `uv sync` installs the qa script globally in venv
- Creates executable: `.venv/bin/qa`
- Also installed in nox environments: `.nox/*/bin/qa`

### 3. User Commands (from README.md)

**Interactive usage**:
```bash
uv run qa check          # Interactive menu with rerun options
uv run qa check --fix-all   # Auto-fix all issues
```

**Individual commands**:
```bash
uv run qa format         # Code + template formatting (ruff + djlint)
uv run qa lint           # Linting only
uv run qa typecheck      # Type checking only
uv run qa newlines       # Newlines checking only
```

### 4. Nox Integration

**Shared configuration**: qa.py imports from noxfile.py for tool consistency
```python
from noxfile import (
    get_djlint_command,
    get_format_command,
    get_lint_command,
    get_typecheck_command,
)
```

**Centralized tool commands** in noxfile.py:
- `LINT_TOOL = ["uv", "tool", "run", "ruff", "check"]`
- `FORMAT_TOOL = ["uv", "tool", "run", "ruff", "format"]`
- `TYPECHECK_TOOL = ["uv", "tool", "run", "mypy"]`
- `DJLINT_TOOL = ["uv", "run", "djlint"]`

### 5. Development Workflow Integration

**Template formatting**: Unified code + template formatting
- Single command `uv run qa format` runs both ruff and djlint
- Automatic detection of templates/ directory

**Quality assurance**: Part of development protocol
- Referenced in CLAUDE.md: "When user says 'qa': Run the individual QA commands"
- Individual commands for targeted checks

## Dependencies

### Direct Dependencies
- `typer==0.17.4` - CLI framework
- `rich==14.1.0` - Terminal formatting
- Built-in: `subprocess`, `pathlib`, `sys`

### Tool Dependencies (via uv)
- `ruff` - Linting and formatting
- `mypy>=1.18.2` - Type checking
- `djlint==1.36.4` - Template formatting
- `pytest-xdist==3.8.0` - Parallel testing

### Integration Dependencies
- `noxfile.py` - Shared tool configuration
- `src/tools/check_newlines.py` - Custom newlines script
- `pytreqt` - Requirements coverage (via `uv run pytreqt show`)

## File Structure

### Current Location
```
src/tools/qa/qa.py       # 934 lines - main implementation
noxfile.py               # Shared tool configurations
src/tools/check_newlines.py  # Custom newlines checking
```

### Installation Creates
```
.venv/bin/qa            # Main executable
.nox/*/bin/qa           # Nox environment executables
```

## Usage Context

### Development Protocol
- Part of quality assurance workflow
- Runs after code changes before commit
- Interactive prompts for fixing issues

### CI/CD Integration
- Could be integrated into GitHub Actions
- Currently uses nox sessions for CI

### User Experience
- Rich terminal interface with colors/emojis
- Interactive menus with single-key navigation
- Database switching (SQLite/PostgreSQL)
- Parallel worker selection (Fibonacci sequence)

## Key Integration Points

### 1. Configuration Sharing
- noxfile.py provides centralized tool configs
- qa.py imports these for consistency
- Fallback implementations if imports fail

### 2. uv Ecosystem Integration
- Uses `uv tool run` for all external tools
- Installed via `uv sync` in project venv
- Modern Python packaging approach

### 3. Template Support
- Automatic detection of templates/ directory
- Unified formatting command for code + templates
- djlint integration for Jinja2/HTML

### 4. Database Testing
- Environment variable switching
- PostgreSQL/SQLite database URLs
- Parallel test execution with pytest-xdist

### 5. Custom Scripts
- Integration with custom newlines checker
- pytreqt requirements coverage reporting
- Extensible for project-specific checks

## Migration Considerations

### Maintain Compatibility
- Keep `uv run qa` command structure
- Preserve all interactive features
- Maintain noxfile.py integration during transition

### Configuration Migration
- Move from noxfile.py imports to pyproject.toml [tool.qa]
- Preserve exact tool commands and paths
- Maintain backwards compatibility

### Installation Method
- Transition from project venv to global uv tool
- `uv tool install qa` instead of `uv sync`
- Keep same CLI interface and behavior