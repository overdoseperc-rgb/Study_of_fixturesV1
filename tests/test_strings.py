import pytest
from strings import string_length, save_string

@pytest.mark.parametrize("value, expected", [("", 0), ("a\nb", 3), ("   ", 3), ("Привет", 6), ("a\r\nb", 4)])
def test_length(value, expected):
    assert string_length(value) == expected

@pytest.mark.parametrize("value", [None, 123, [], b"abc"])
def test_invalid_type(value, tmp_path):
    with pytest.raises(TypeError):
        string_length(value)
    with pytest.raises(TypeError):
        save_string(value, tmp_path / "invalid.txt")
    assert not (tmp_path / "invalid.txt").exists()

@pytest.mark.parametrize("already_exists", [False, True])
def test_save(text_value, already_exists, tmp_path):
    path = tmp_path / "result.txt"
    if already_exists:
        path.write_text("Старое содержимое длиннее нового", encoding="utf-8")
    assert save_string(text_value, path) == path
    assert path.read_bytes() == text_value.encode("utf-8")
