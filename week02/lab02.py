def make_greeting(name: str) -> str:
    return f"Hello, {name}!"


def is_even(number: int) -> bool:
    return number % 2 == 0


def count_vowels(text: str) -> int:
    """Count a, e, i, o, and u without regard to case; do not count y."""
    return sum(1 for character in text.lower() if character in "aeiou")