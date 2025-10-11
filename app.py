from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello Container</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
            padding-top: 100px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 15px 30px;
            font-size: 18px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
        }
        h2 {
            color: #333;
            margin-top: 40px;
        }
    </style>
</head>
<body>
    <h1>زايد جاى يا شوية ديف اوبس</h1>
    <form method="post">
        <button type="submit">Click Me</button>
    </form>
    {% if message %}
    <h2>{{ message }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    if request.method == "POST":
        message = "Hello from container Ahmed Zayed!"
    return render_template_string(HTML_PAGE, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8070)
