from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello Container</title>
    <meta charset="utf-8">
    <style>
        /* Basic layout (kept simple so functionality isn't changed) */
        html, body {
            height: 100%;
            margin: 0;
        }
        body {
            font-family: "Courier New", Courier, monospace;
            background: #050505;              /* deep black */
            color: #00ff66;                   /* neon green-ish */
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            padding-top: 80px;
            overflow: hidden;
        }

        /* Matrix-style canvas fills the screen behind content */
        #matrix {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            pointer-events: none; /* don't intercept clicks */
            opacity: 0.18;
            mix-blend-mode: screen;
        }

        /* Content container sits above canvas */
        .shell {
            position: relative;
            z-index: 2;
            width: 90%;
            max-width: 760px;
            backdrop-filter: blur(0px);
        }

        h1 {
            margin: 0 0 24px 0;
            font-size: 30px;
            letter-spacing: 2px;
            color: #00ff66;
            text-shadow: 0 0 8px rgba(0,255,102,0.18), 0 0 20px rgba(0,255,102,0.06);
        }

        /* keep button label & behaviour the same as you requested */
        form {
            margin-top: 10px;
        }

        button {
            background-color: transparent;
            color: #00ff66;
            padding: 12px 28px;
            font-size: 16px;
            border: 2px solid rgba(0,255,102,0.6);
            border-radius: 8px;
            cursor: pointer;
            transition: all 180ms ease;
            box-shadow: 0 0 8px rgba(0,255,102,0.06);
        }
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 0 18px rgba(0,255,102,0.18);
            background: rgba(0,51,0,0.08);
        }

        /* message text styled but same semantics (h2 present if message) */
        h2 {
            margin-top: 34px;
            color: #00ff66;
            font-size: 20px;
            letter-spacing: 1px;
            text-shadow: 0 0 6px rgba(0,255,102,0.12);
        }

        /* small footer / ambiguous status line */
        .status {
            margin-top: 26px;
            font-size: 12px;
            opacity: 0.7;
            color: #7aff9a;
            letter-spacing: 1px;
        }

        /* subtle glitch-like effect for heading without changing content */
        @keyframes slight-glitch {
            0% { transform: translateX(0px); }
            30% { transform: translateX(-1px); }
            60% { transform: translateX(1px); }
            100% { transform: translateX(0px); }
        }
        h1 { animation: slight-glitch 3s infinite linear; }

        /* ensure content remains readable on small screens */
        @media (max-width: 420px) {
            h1 { font-size: 22px; }
            button { padding: 10px 18px; font-size: 14px; }
            h2 { font-size: 16px; }
        }
    </style>
</head>
<body>
    <!-- matrix canvas background (pure client-side, non-blocking) -->
    <canvas id="matrix" aria-hidden="true"></canvas>

    <div class="shell" role="main">
        <!-- keep your Arabic header exactly as provided -->
        <h1>This too shall pass !</h1>

        <form method="post">
            <button type="submit">Click Me</button>
        </form>

        {% if message %}
        <h2>{{ message }}</h2>
        {% endif %}

        <div class="status">ACCESS: █████▒▒▒▒  |  SESSION: ~anonymous~</div>
    </div>

    <script>
    // Matrix-like falling characters background.
    // Lightweight and unobtrusive: won't change your page structure or POST behavior.
    (function() {
        const canvas = document.getElementById('matrix');
        const ctx = canvas.getContext('2d');
        let w = canvas.width = window.innerWidth;
        let h = canvas.height = window.innerHeight;
        const cols = Math.floor(w / 18);
        const ypos = new Array(cols).fill(0);

        const chars = "0123456789abcdefghijklmnopqrstuvwxyz@#$%&*?=+-".split('');

        function draw() {
            ctx.fillStyle = 'rgba(5,5,5,0.18)';
            ctx.fillRect(0, 0, w, h);

            ctx.fillStyle = '#00ff66';
            ctx.font = '14px Courier New';

            for (let i = 0; i < cols; i++) {
                const text = chars[Math.floor(Math.random() * chars.length)];
                const x = i * 18;
                const y = ypos[i] * 18;

                // Slight alpha variation for nicer look
                ctx.fillStyle = 'rgba(0,255,102,' + (0.4 + Math.random()*0.6) + ')';
                ctx.fillText(text, x, y);

                if (y > h && Math.random() > 0.975) {
                    ypos[i] = 0;
                } else {
                    ypos[i]++;
                }
            }
        }

        let raf;
        function loop() {
            draw();
            raf = requestAnimationFrame(loop);
        }
        loop();

        // handle resize
        window.addEventListener('resize', function() {
            cancelAnimationFrame(raf);
            w = canvas.width = window.innerWidth;
            h = canvas.height = window.innerHeight;
            const newCols = Math.floor(w / 18);
            ypos.length = newCols;
            for (let i = 0; i < newCols; i++) ypos[i] = ypos[i] || 0;
            loop();
        }, {passive: true});
    })();
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    if request.method == "POST":
        message = "k e e p      g o i n g , p u s h   m o r e  .."
    return render_template_string(HTML_PAGE, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8070)
