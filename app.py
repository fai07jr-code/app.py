from flask import Flask, request, jsonify
import random
import datetime

app = Flask(__name__)

# --- транслитерация ---
def translit(text):
    mapping = {
        'А':'A','Б':'B','В':'V','Г':'G','Д':'D',
        'Е':'E','Ё':'E','Ж':'ZH','З':'Z','И':'I',
        'Й':'Y','К':'K','Л':'L','М':'M','Н':'N',
        'О':'O','П':'P','Р':'R','С':'S','Т':'T',
        'У':'U','Ф':'F','Х':'H','Ц':'TS','Ч':'CH',
        'Ш':'SH','Щ':'SCH','Ы':'Y','Э':'E','Ю':'YU','Я':'YA'
    }

    text = text.upper()
    result = ''

    for char in text:
        result += mapping.get(char, char)

    return result[:3]


@app.route('/generate', methods=['GET'])
def generate():
    last_name = request.args.get('name', 'NON')

    short = translit(last_name)

    now = datetime.datetime.now()
    day = str(now.day).zfill(2)
    month = str(now.month).zfill(2)
    year = str(now.year)[-2:]

    number = random.randint(100, 999)

    order_id = f"{short}-{day}.{month}.{year}-{number}-VRN"

    return jsonify({
        "order_id": order_id
    })

