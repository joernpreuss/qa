# QA Tool References Analysis

Complete analysis of where qa tool is referenced in the source project.

## Direct References

### 1. Package Configuration
**File**: `pyproject.toml`
```toml
[project.scripts]
qa = "src.tools.qa.qa:main"
```
- Creates `qa` executable in venv via `uv sync`

### 2. Documentation
**File**: `README.md` (4 references)
```bash
uv run qa check          # Interactive menu with rerun options
uv run qa check --fix-all   # Auto-fix all issues
uv run qa format         # Individual commands
uv run qa lint
uv run qa typecheck
uv run qa newlines
```

**File**: `CLAUDE.md` (1 reference)
- Development instruction: "When user says 'qa': Run the individual QA commands (not `uv run qa` tool)"

**File**: `docs/DEVELOPMENT.md` (2 references)
- Template formatting integration
- Individual commands documentation

### 3. Implementation Files
**File**: `src/tools/qa/qa.py` (934 lines)
- Main implementation
- Self-reference as "SAVT Quality Assurance Tool"

**File**: `noxfile.py` (indirect integration)
- Provides shared tool configurations
- qa.py imports: `get_lint_command`, `get_format_command`, etc.

## Integration Points

### 1. Tool Dependencies
**Referenced in qa.py**:
- `typer==0.17.4` - CLI framework
- `rich==14.1.0` - Terminal formatting
- `djlint==1.36.4` - Template formatting
- `pytest-xdist==3.8.0` - Parallel testing
- `mypy>=1.18.2` - Type checking

### 2. Custom Scripts Integration
**File**: `src/tools/check_newlines.py`
- Referenced in qa.py for trailing newlines checking
- Path: `tools_dir / "check_newlines.py"`

### 3. Requirements Coverage
**Command**: `uv run pytreqt show`
- Referenced in qa.py for coverage reporting
- Function: `_show_requirements_coverage()`

## CI/CD Integration

### Current CI (.github/workflows/ci.yml)
**Status**: ❌ **Does NOT use qa tool**

**Current approach**: Direct tool calls
```yaml
- name: Run linter
  run: uv tool run ruff check src/ tests/

- name: Check formatting
  run: uv tool run ruff format src/ tests/ --check

- name: Run type checker
  run: uv tool run mypy src/
```

**Alternative**: Could use qa tool
```yaml
- name: Run QA checks
  run: uv run qa check --fix-all
```

### Deployment Pipeline
**File**: `.github/workflows/deploy.yml`
- No qa tool references found
- Uses standard deployment workflow

## Installation Integration

### Virtual Environment
**Command**: `uv sync --all-extras --dev`
- Installs qa as executable: `.venv/bin/qa`
- Available as `uv run qa` in project

### Nox Environments
**Multiple installations**:
```
.nox/format_check-3-13/bin/qa
.nox/mypy-3-13/bin/qa
.nox/lint-3-13/bin/qa
.nox/djlint_check-3-13/bin/qa
```

## Usage Patterns

### Development Workflow
1. **Interactive usage**: `uv run qa i` for menu-driven QA
2. **Batch fixing**: `uv run qa check --fix-all`
3. **Targeted checks**: `uv run qa format`, `uv run qa lint`

### Template Integration
- Unified formatting: code + templates in single command
- Automatic templates/ directory detection
- djlint + ruff coordination

### Database Testing
- Environment variable configuration
- SQLite/PostgreSQL switching
- Parallel test execution

## Migration Impact Analysis

### Files Requiring Updates

#### 1. README.md
**Current**: `uv run qa check`
**Future**: `qa check` (global tool)

#### 2. CLAUDE.md
**Current**: Reference to `uv run qa` tool
**Future**: Reference to global `qa` command

#### 3. docs/DEVELOPMENT.md
**Current**: `uv run qa format` examples
**Future**: `qa format` examples

#### 4. pyproject.toml
**Action**: Remove `[project.scripts]` section
**Reason**: qa becomes global tool, not project dependency

#### 5. CI/CD (Optional Enhancement)
**Current**: Individual tool commands
**Future**: Could use `qa check --fix-all` for unified QA

### Files NOT Requiring Updates

#### Source Code
- `src/tools/qa/qa.py` - Will be extracted/generalized
- `noxfile.py` - Remains for backwards compatibility
- `src/tools/check_newlines.py` - Remains as custom script

#### Dependencies
- Core dependencies move to global qa-tool package
- Project-specific tools remain in pyproject.toml

## Reference Summary

**Total References**: 10 files
- **Configuration**: 1 (pyproject.toml)
- **Documentation**: 4 (README, CLAUDE, DEVELOPMENT, planning)
- **Implementation**: 2 (qa.py, noxfile.py integration)
- **Installation**: 3 (venv, nox environments, planning doc)

**Migration Complexity**: **Low-Medium**
- Most references are documentation updates
- No complex interdependencies
- Clear separation between tool and project code
- CI/CD integration is optional enhancement