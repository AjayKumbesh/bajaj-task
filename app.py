from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# CONFIG - customize these with your own details for submission
FULL_NAME = "john_doe"
DOB = "17091999"     # ddmmyyyy
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

# Helper function for alternating caps in reverse
def alternating_caps(s):
    result = ""
    upper = True
    for c in reversed(s):
        if c.isalpha():
            result += c.upper() if upper else c.lower()
            upper = not upper
    return result

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.json.get('data', [])
        even_numbers, odd_numbers, alphabets, specials = [], [], [], []
        sum_numbers = 0
        concat_alpha = ""

        for item in data:
            item_str = str(item)
            if item_str.isdigit():
                num = int(item_str)
                sum_numbers += num
                if num % 2 == 0:
                    even_numbers.append(item_str)
                else:
                    odd_numbers.append(item_str)
            elif re.match(r'^[a-zA-Z]+$', item_str):
                alphabets.append(item_str.upper())
                concat_alpha += item_str
            else:
                specials.append(item_str)

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME.lower()}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": specials,
            "sum": str(sum_numbers),
            "concat_string": alternating_caps(concat_alpha)
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

if __name__ == "__main__":
    app.run()
