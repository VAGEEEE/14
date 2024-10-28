def count_vowels(text):
    """Підраховує кількість голосних у тексті."""
    vowels = "аеєиіїоуюяaeiou"
    return sum(1 for char in text.lower() if char in vowels)
