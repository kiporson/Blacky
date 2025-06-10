from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>DIABLO Chart Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: monospace; background: #0f0f0f; color: #00ff99; padding: 2em; }
        h1 { color: white; }
        canvas { background: #111; border-radius: 10px; padding: 1em; }
    </style>
</head>
<body>
    <h1>📊 DIABLO Earnings Chart</h1>
    <canvas id="earningChart" width="800" height="400"></canvas>

    <script>
        const ctx = document.getElementById('earningChart').getContext('2d');
        const chart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: {{ labels|safe }},
                datasets: [{
                    label: 'Earnings ($)',
                    data: {{ data|safe }},
                    backgroundColor: '#00ff99'
                }]
            },
            options: {
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    </script>
</body>
</html>
'''

@app.route("/")
def dashboard():
    con = sqlite3.connect("vault/earnings.db")
    cur = con.cursor()
    rows = cur.execute("SELECT source, amount FROM earnings ORDER BY id DESC LIMIT 10").fetchall()
    con.close()

    labels = [r[0] for r in rows]
    data = [r[1] for r in rows]
    return render_template_string(TEMPLATE, labels=labels, data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
