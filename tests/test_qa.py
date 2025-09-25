"""Basic test to ensure package imports correctly."""

import qa


def test_version() -> None:
    """Test that version is defined."""
    assert hasattr(qa, "__version__")
    assert qa.__version__ == "0.1.0"
