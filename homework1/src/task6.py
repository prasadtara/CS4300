from pathlib import Path
from typing import Union

def count_words_in_file(path: Union[str, Path]) -> int:
    text = Path(path).read_text(encoding="utf-8")
    return len(text.split())


def main() -> None:
    here = Path(__file__).resolve()
    homework1_dir = here.parents[1]
    file_path = homework1_dir / "task6_read_me.txt"
    print(count_words_in_file(file_path))


if __name__ == "__main__":
    main()
