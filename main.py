import re

def custom_sort_key(word):
    ukr_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    ukr_lower = {char: i for i, char in enumerate(ukr_alphabet)}
    eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
    eng_lower = {char: i + len(ukr_alphabet) for i, char in enumerate(eng_alphabet)}

    def get_char_value(char):
        lower_char = char.lower()
        if lower_char in ukr_lower:
            return ukr_lower[lower_char]
        elif lower_char in eng_lower:
            return eng_lower[lower_char]
        return float('inf')  # Невідомий символ

    return [get_char_value(c) for c in word]

def read_first_sentence(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().strip()
            first_sentence = re.split(r'[.!?]', text)[0]
            return first_sentence
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    return None

def sort_words(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    sorted_words = sorted(words, key=custom_sort_key)
    return sorted_words

def main():
    file_path = 'text.txt'

    sentence = read_first_sentence(file_path)

    if sentence:
        print("Перше речення:")
        print(sentence)

        sorted_words = sort_words(sentence)

        print("Відсортовані слова:")
        print(sorted_words)

        print(f"Кількість слів: {len(sorted_words)}")

if __name__ == "__main__":
    main()

