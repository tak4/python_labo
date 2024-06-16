from typing import List

# List[int] で要素が int のリスト型を表す型ヒントになる
def load_numbers_sorted(txt: str) -> List[int]:
    numbers = []

    with open(txt) as f:
        numbers = sorted(map(lambda e: int(e), f))

    return numbers