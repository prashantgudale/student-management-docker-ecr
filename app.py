from flask import Flask
import pandas as pd
import os

app = Flask(__name__)

EXCEL_FILE = "students.xlsx"

@app.route("/")
def home():

    if not os.path.exists(EXCEL_FILE):
        return "Student Excel file not found!", 404

    df = pd.read_excel(EXCEL_FILE)

    html = """
    <html>
    <head>
        <title>Student Management System</title>
        <style>
            body {
                font-family: Arial;
                background: #f2f2f2;
                padding: 30px;
            }

            h1 {
                color: #154360;
                text-align: center;
            }

            table {
                width: 80%;
                margin: auto;
                border-collapse: collapse;
                background: white;
            }

            th, td {
                border: 1px solid #ddd;
                padding: 12px;
                text-align: center;
            }

            th {
                background: #2874A6;
                color: white;
            }
        </style>
    </head>

    <body>

        <h1>Student Management System</h1>

        <h3 style="text-align:center;">
            Student Records from Excel
        </h3>

        """

    html += df.to_html(index=False, border=0, classes="student-table")

    html += """
    </body>
    </html>
    """

    return html


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
