import os
import random
from colorama import init, Fore, Style

# Ініціалізація colorama
init(autoreset=True)

def load_words_from_file(filename):
    """Завантажити слова з файлу."""
    if not os.path.isfile(filename):
        print(Fore.RED + f"Файл {filename} не знайдено. Перевірте шлях до файлу.")
        return {}
    
    words = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(';')
                if len(parts) == 4:
                    word, article, part_of_speech, translation = parts
                    words[word] = {
                        "article": article,
                        "part_of_speech": part_of_speech,
                        "translation": translation
                    }
                else:
                    print(Fore.YELLOW + f"Неправильний формат рядка: {line.strip()}")
    except Exception as e:
        print(Fore.RED + f"Помилка при читанні файлу: {e}")
        return {}
    
    if not words:
        print(Fore.YELLOW + "Файл не містить жодних даних.")
    return words

# Завантажуємо слова з файлу
words_with_details = load_words_from_file('D:\\Pyton\\words_data.txt')

def get_random_word():
    """Отримати випадкове німецьке слово з артиклем та частиною мови."""
    if not words_with_details:
        print(Fore.RED + "Словник порожній. Додайте слова до файлу.")
        return None, None
    
    word = random.choice(list(words_with_details.keys()))
    details = words_with_details[word]
    return word, details

def print_word_info(word, details):
    """Функція для форматування і друку інформації про слово з покращеним графічним відображенням."""
    separator = "=" * 50
    print(Fore.LIGHTBLACK_EX + separator)  # Сірий separator
    
    # Виводимо опис сірим кольором
    print(Fore.LIGHTBLACK_EX + f"Німецьке слово:        ", end='')
    
    # Виводимо німецьке слово білим кольором
    if details["article"] != "N/A":
        print(Fore.WHITE + f"{details['article']} {word}")
    else:
        print(Fore.WHITE + f"{word}")
    
    # Виводимо частину мови та переклад сірим кольором
    print(Fore.LIGHTBLACK_EX + f"Частина мови:          {details['part_of_speech']}")
    print(Fore.LIGHTBLACK_EX + f"Переклад (українською): ", end='')
    
    # Виводимо переклад білим кольором
    print(Fore.WHITE + f"{details['translation']}")
    
    print(Fore.LIGHTBLACK_EX + separator)  # Сірий separator
    print()  # Пустий рядок для відступу

def main():
    print(Fore.WHITE + "Натискайте Enter для перегляду нових слів. Натисніть 'q' для виходу.")
    
    while True:
        user_input = input()
        if user_input.lower() == 'q':
            break
        
        word, details = get_random_word()
        if word and details:
            print_word_info(word, details)
        else:
            print(Fore.RED + "Не вдалося отримати інформацію про слово.")

if __name__ == "__main__":
    main() 