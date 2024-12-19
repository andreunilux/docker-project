# File: tests/test_main_menu.py
from unittest.mock import patch
from app import handle_menu_choice

def test_handle_menu_choice_exit(capsys):
    """
    Test that the application exits gracefully when option 2 is selected.
    """
    with patch("builtins.exit") as mock_exit:
        handle_menu_choice("2")
        mock_exit.assert_called_once_with(0)

def test_handle_menu_choice_invalid(capsys):
    """
    Test that an invalid menu choice produces the correct error message.
    """
    handle_menu_choice("invalid")
    captured = capsys.readouterr()
    assert "Invalid choice" in captured.out
