from flask import Flask, render_template_string, request, send_file
import base64
import requests
import io

app = Flask(__name__)

HTML_PAGE = """
<!-- your existing HTML -->
<form method="post">
    <button type="submit" name="action" value="click_me">Click Me</button>
    <button type="submit" name="action" value="get_config">Get Configuration</button>
</form>
{% if message %}
<h2>{{ message }}</h2>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    if request.method == "POST":
        action = request.form.get("action")
        if action == "click_me":
            message = "k e e p      g o i n g , p u s h   m o r e  .."
        elif action == "get_config":
            # API credentials
            cred = "Admin:Admin"
            cred_encoded = base64.b64encode(cred.encode()).decode()
            url = "http://192.168.128.144/api/v1/files/ini"
            headers = {"Authorization": f"Basic {cred_encoded}"}

            try:
                response = requests.get(url, headers=headers, timeout=5)
                if response.status_code == 200:
                    # Create a BytesIO object to send as a file
                    file_stream = io.BytesIO(response.content)
                    file_stream.seek(0)
                    return send_file(
                        file_stream,
                        as_attachment=True,
                        download_name="INI3.txt",
                        mimetype="text/plain"
                    )
                else:
                    message = f"Failed to fetch configuration (HTTP {response.status_code})"
            except Exception as e:
                message = f"Error: {str(e)}"

    return render_template_string(HTML_PAGE, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8070)
