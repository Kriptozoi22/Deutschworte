from flask import Flask, render_template, jsonify
import random
import os

app = Flask(__name__)

def load_words_from_file(filename):
    """Завантажити слова з файлу."""
    if not os.path.isfile(filename):
        print(f"Файл {filename} не знайдено. Перевірте шлях до файлу.")
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
                    print(f"Неправильний формат рядка: {line.strip()}")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return {}
    
    if not words:
        print("Файл не містить жодних даних.")
    return words

# Завантажуємо слова з файлу
words_with_details = load_words_from_file('D:\\Pyton\\words_data.txt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_word')
def get_word():
    """Отримати випадкове слово з артиклем та частиною мови."""
    if not words_with_details:
        return jsonify({'error': 'No words available'}), 404
    
    word = random.choice(list(words_with_details.keys()))
    details = words_with_details[word]
    return jsonify({
        'word': f"{details['article']} {word}",
        'part_of_speech': details['part_of_speech'],
        'translation': details['translation']
    })

if __name__ == '__main__':
    app.run(debug=True)
