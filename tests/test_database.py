import pytest

@pytest.mark.parametrize("value", ["", "   ", "Первая\nВторая", "O'Reilly"])
def test_database_isolation(db, value):
    # Каждая параметризация получает пустую БД независимо от порядка запуска.
    assert db.execute("SELECT COUNT(*) FROM strings").fetchone()[0] == 0
    db.execute("INSERT INTO strings(value) VALUES (?)", (value,))
    db.commit()
    assert db.execute("SELECT value FROM strings").fetchall() == [(value,)]
