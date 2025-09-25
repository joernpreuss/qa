# QA Tool CLI Commands Documentation

Complete documentation of all CLI commands from source project's qa.py (934 lines).

## Main Commands

### `qa check` (Default Command)
**Function**: `check()` at line 315
**Description**: Run all QA checks with optional fixes

```bash
qa check                   # Run all checks (no fixes)
qa check /path/to/project  # Run checks on specific path
qa check --fix-all         # Run checks with all fixes
qa check --fix-format      # Fix formatting only
qa check --fix-lint        # Fix linting only
qa check --fix-newlines    # Fix newlines only
qa check --unsafe-fixes    # Enable unsafe fixes for linting
qa check --skip-tests      # Skip test execution
```

**Parameters**:
- `path: str = "."` - Project directory path
- `fix_all: bool = False` - Auto-fix all issues
- `fix_format: bool = False` - Fix formatting only
- `fix_lint: bool = False` - Fix linting only
- `fix_newlines: bool = False` - Fix newlines only
- `unsafe_fixes: bool = False` - Enable unsafe lint fixes
- `skip_tests: bool = False` - Skip test execution

**Behavior**:
1. Runs format check → lint check → typecheck → newlines check
2. Shows interactive fix/skip/quit prompts for each failing check
3. Displays requirements coverage at the end
4. Offers test execution menu (database selection + parallel workers)

### `qa fix-all` (Shortcut Command)
**Function**: `fix_all_command()` at line 772
**Description**: Shortcut for `qa check --fix-all`

```bash
qa fix-all        # Equivalent to 'qa check --fix-all'
```

### `qa format`
**Function**: `format_command()` at line 790
**Description**: Run code and template formatters

```bash
qa format               # Format code and templates
qa format --check       # Check formatting only (no changes)
qa format /path         # Format specific path
```

**Parameters**:
- `path: str = "."` - Project directory path
- `check: bool = False` - Check formatting only

**Tools Used**:
- **Code**: `ruff format src/ tests/` (via noxfile)
- **Templates**: `djlint templates/` (if templates/ exists)

### `qa lint`
**Function**: `lint_command()` at line 844
**Description**: Run linter with optional fixes

```bash
qa lint                 # Check linting issues
qa lint --fix           # Fix linting issues
qa lint --unsafe        # Enable unsafe fixes
qa lint /path           # Lint specific path
```

**Parameters**:
- `path: str = "."` - Project directory path
- `fix: bool = False` - Auto-fix issues
- `unsafe: bool = False` - Enable unsafe fixes

**Tool Used**: `ruff check src/ tests/` (via noxfile)

### `qa typecheck`
**Function**: `typecheck_command()` at line 875
**Description**: Run type checker

```bash
qa typecheck            # Run mypy type checking
qa typecheck /path      # Typecheck specific path
```

**Parameters**:
- `path: str = "."` - Project directory path

**Tool Used**: `mypy src/ tests/` (via noxfile)

### `qa newlines`
**Function**: `newlines_command()` at line 891
**Description**: Check/fix trailing newlines

```bash
qa newlines             # Check trailing newlines
qa newlines --fix       # Fix trailing newlines
qa newlines /path       # Check specific path
```

**Parameters**:
- `path: str = "."` - Project directory path
- `fix: bool = False` - Auto-fix missing newlines

**Implementation**: Custom script at `src/tools/check_newlines.py`

### `qa i` (Interactive Mode)
**Function**: `interactive()` at line 918
**Description**: Launch interactive menu system

```bash
qa i                    # Start interactive mode
```

**Features**:
- Single-key navigation (f/s/q prompts for each check)
- Database selection menu (SQLite/PostgreSQL)
- Parallel worker selection (Fibonacci sequence: 1,2,3,5,8,13,21,34,55,89,120,160,200)
- Requirements coverage display
- ESC key support for quick quit
- Rich terminal output with colors and emojis

## Interactive Menu System

### Fix/Skip/Quit Prompts
**Function**: `_prompt_fix_skip_quit()` at line 130

For each failing check, prompts:
- `f` - Fix the issue
- `s` - Skip this check
- `q` - Quit entirely
- `ESC` - Quick exit

### Database Test Menu
**Function**: `_interactive_menu()` at line 420

Options:
1. **SQLite Tests** - Use `sqlite:///./test.db`
2. **PostgreSQL Tests** - Use `postgresql://savt_user:savt_password@localhost:5432/savt`
3. **Skip Tests**
4. **Change Parallel Workers** (Fibonacci sequence selection)

### Parallel Worker Selection
**Available workers**: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 120, 160, 200
**Implementation**: Interactive menu with number selection

## Internal Functions

### Core Check Functions
- `_run_individual_check()` - Execute single check with fix/skip/quit prompt
- `_run_command()` - Execute shell commands with rich output
- `_run_checks()` - Main check orchestration with interactive prompts

### Database Testing
- `_run_database_tests()` - Execute tests with specific database configuration
- Environment variables: `TEST_DATABASE`, `DATABASE_URL`

### File Operations
- `_check_trailing_newlines()` - Main newlines checking logic
- `_check_trailing_newlines_fallback()` - Fallback implementation
- `_check_newlines_impl()` - Core newlines checking
- `_has_templates_directory()` - Check for templates/ directory

### Interactive Utilities
- `_get_single_key()` - Capture single keypress input
- `_prompt_single_key()` - Generic single-key prompt system
- `_show_requirements_coverage()` - Display pytreqt coverage

## Rich Terminal Features

### Colors and Emojis
- ✅ Green checkmarks for passing checks
- ❌ Red X marks for failing checks
- 🧪 Test selection menus
- 🚀 Performance indicators
- Rich progress bars and formatting

### Output Formatting
- Clear section headers
- Indented command output
- Colored status messages
- Interactive prompts with highlights

## Environment Variables

### Database Configuration
- `TEST_DATABASE=postgresql|sqlite` - Database type selection
- `DATABASE_URL=postgresql://...` - PostgreSQL connection string
- `DATABASE_URL=sqlite:///./test.db` - SQLite database file

### Test Execution
- `pytest --color=yes` with parallel workers: `-n{worker_count}`

## Error Handling

### Command Failures
- Non-zero exit codes trigger fix/skip/quit prompts
- Rich error display with command details
- Graceful handling of missing tools/dependencies

### Interactive Flow
- ESC key support for immediate exit
- Invalid input handling with re-prompts
- Clean error messages for user guidance

## Configuration Integration

### Nox Function Imports
```python
from noxfile import (
    get_djlint_command,
    get_format_command,
    get_lint_command,
    get_typecheck_command,
)
```

### Fallback Implementations
Complete fallback implementations when noxfile imports fail, using hardcoded source project-specific paths and tools.

## Performance Features

### Parallel Test Execution
- Fibonacci sequence workers: 1→200 workers
- pytest-xdist integration: `pytest -n{workers}`
- Interactive worker count selection

### Fast Command Execution
- All tools via `uv tool run` for speed
- Rich output for immediate feedback
- Subprocess optimization for large codebases

---

**Total Implementation**: 934 lines of sophisticated QA tooling with rich interactive features, database testing, parallel execution, and comprehensive error handling.