from src.task5 import favorite_books, first_three_books, student_database

def test_first_three_books():
    books = favorite_books()
    assert first_three_books(books) == books[:3]
    assert len(first_three_books(books)) == 3

def test_student_database_structure():
    db = student_database()
    assert isinstance(db, dict)
    assert db["Ada Lovelace"] == "S001"
