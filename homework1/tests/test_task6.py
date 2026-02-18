from pathlib import Path
from src.task6 import count_words_in_file

def test_word_count_task6_read_me():
    homework1_dir = Path(__file__).resolve().parents[1]
    path = homework1_dir / "task6_read_me.txt"
    assert path.exists()
    assert count_words_in_file(path) == len(path.read_text(encoding="utf-8").split())
