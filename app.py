from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        message = request.form.get("message", "")

    return f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MyChat</title>

<style>
body {{
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f0f2f5;
}}

.header {{
    background: #128C7E;
    color: white;
    padding: 18px;
    font-size: 24px;
    font-weight: bold;
}}

.chat {{
    padding: 20px;
    padding-bottom: 80px;
}}

.message {{
    background: white;
    padding: 12px;
    border-radius: 10px;
    margin: 10px 0;
    max-width: 75%;
}}

.send {{
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    display: flex;
    padding: 10px;
    background: white;
    box-sizing: border-box;
}}

input {{
    flex: 1;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 20px;
}}

button {{
    margin-left: 8px;
    background: #128C7E;
    color: white;
    border: none;
    border-radius: 20px;
    padding: 12px 20px;
}}
</style>
</head>

<body>

<div class="header">
💬 MyChat
</div>

<div class="chat">

<div class="message">
سلام! 👋
</div>

<div class="message">
MyChat ته ښه راغلاست.
</div>

{f'<div class="message">{message}</div>' if message else ''}

</div>

<form class="send" method="POST">
<input name="message" type="text" placeholder="پیغام ولیکئ..." required>
<button type="submit">Send</button>
</form>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
