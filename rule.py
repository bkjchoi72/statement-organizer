from typing import List

from enumeration.category import Category


class Rule:
    def __init__(self, category: Category):
        self.category: Category = category
        self.substrings: List[str] = []

    def __eq__(self, other):
        return self.category == other.category

    def add_rule(self, substring: str):
        if substring not in self.substrings:
            self.substrings.append(substring)

    def satisfies(self, description: str) -> bool:
        for substring in self.substrings:
            if substring.lower().strip() in description.lower().strip():
                return True
        return False
