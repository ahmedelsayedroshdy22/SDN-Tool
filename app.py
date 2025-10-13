from flask import Flask, render_template_string, request, send_file
import base64
import requests
import io

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Control Panel</title>

    <!-- Bootstrap 5 CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
        body {
            background-color: #f5f7fa;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        .card {
            border-radius: 1rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            padding: 2rem;
            background: white;
        }

        h1 {
            margin-bottom: 1.5rem;
            font-weight: 600;
            color: #333;
        }

        .btn {
            min-width: 180px;
            margin: 0.5rem;
            font-weight: 500;
            border-radius: 0.6rem;
        }

        h2 {
            margin-top: 2rem;
            color: #0d6efd;
        }
    </style>
</head>
<body>
    <div class="card text-center">
        <h1>System Control Panel</h1>

        <form method="post">
            <div class="d-flex flex-wrap justify-content-center">
                <!-- Existing Buttons -->
                <button type="submit" name="action" value="click_me" class="btn btn-primary">Click Me</button>
                <button type="submit" name="action" value="get_config" class="btn btn-secondary">Get Configuration</button>

                <!-- New Buttons -->
                <button type="submit" name="action" value="restart" class="btn btn-warning">Restart</button>
                <button type="submit" name="action" value="shutdown" class="btn btn-danger">Shutdown</button>
                <button type="submit" name="action" value="status" class="btn btn-info">Check Status</button>
                <button type="submit" name="action" value="logs" class="btn btn-success">View Logs</button>
            </div>
        </form>

        {% if message %}
        <h2>{{ message }}</h2>
        {% endif %}
    </div>

    <!-- Bootstrap JS Bundle -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

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
