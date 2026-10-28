from flask import Flask, render_template_string, request

app = Flask(__name__)

DEFAULT_FORM_VALUES = {
    "college_name": "Green Valley College",
    "class_start": "09:00",
    "class_end": "10:30",
    "break_start": "10:30",
    "break_end": "10:45",
    "student_text": "No message entered yet",
}


def get_form_values():
    values = DEFAULT_FORM_VALUES.copy()

    if request.method == "POST":
        for key, default_value in DEFAULT_FORM_VALUES.items():
            submitted_value = request.form.get(key, default_value)
            if submitted_value:
                values[key] = submitted_value

    return values


def get_status(student_text):
    if student_text and student_text.strip():
        return "Attendance sent successfully"
    return "Please enter student message"


HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>College Attendance Smart System</title>
    <style>
        * { box-sizing: border-box; }
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #dbeafe, #f8fafc);
            color: #111827;
        }
        .container {
            max-width: 1000px;
            margin: 50px auto;
            background: #fff;
            border-radius: 18px;
            box-shadow: 0 12px 30px rgba(0,0,0,0.12);
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #0f172a, #2563eb);
            color: white;
            padding: 25px;
            text-align: center;
        }
        .header h1 {
            margin: 0;
            font-size: 2rem;
        }
        .main {
            display: grid;
            grid-template-columns: 1.2fr 0.8fr;
            gap: 24px;
            padding: 30px;
        }
        .panel {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 14px;
            padding: 22px;
        }
        h2 {
            margin-top: 0;
            margin-bottom: 18px;
            color: #0f172a;
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
        }
        input, textarea {
            width: 100%;
            padding: 12px 14px;
            margin-bottom: 18px;
            border: 1px solid #cbd5e1;
            border-radius: 10px;
            font-size: 1rem;
        }
        input:focus, textarea:focus {
            outline: none;
            border-color: #2563eb;
            box-shadow: 0 0 0 3px rgba(37,99,235,0.15);
        }
        .row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }
        textarea {
            min-height: 120px;
            resize: vertical;
        }
        button {
            width: 100%;
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 14px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
        }
        button:hover {
            background: linear-gradient(135deg, #1d4ed8, #1e40af);
        }
        .summary p {
            margin: 12px 0;
            font-size: 1rem;
        }
        .status {
            margin-top: 20px;
            background: #dbeafe;
            color: #1e3a8a;
            border-radius: 10px;
            padding: 12px 14px;
            font-weight: bold;
        }
        @media (max-width: 768px) {
            .main {
                grid-template-columns: 1fr;
            }
            .row {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>College Attendance Smart System</h1>
        </div>

        <div class="main">
            <div class="panel">
                <h2>Attendance Details</h2>
                <form method="POST">
                    <label for="college_name">College Name</label>
                    <input type="text" id="college_name" name="college_name" value="{{ college_name }}" required>

                    <div class="row">
                        <div>
                            <label for="class_start">Class Start</label>
                            <input type="time" id="class_start" name="class_start" value="{{ class_start }}" required>
                        </div>
                        <div>
                            <label for="class_end">Class End</label>
                            <input type="time" id="class_end" name="class_end" value="{{ class_end }}" required>
                        </div>
                    </div>

                    <div class="row">
                        <div>
                            <label for="break_start">Break Start</label>
                            <input type="time" id="break_start" name="break_start" value="{{ break_start }}" required>
                        </div>
                        <div>
                            <label for="break_end">Break End</label>
                            <input type="time" id="break_end" name="break_end" value="{{ break_end }}" required>
                        </div>
                    </div>

                    <label for="student_text">Student Text / Message</label>
                    <textarea id="student_text" name="student_text" placeholder="Example: Student present for Java Lab, Rahul, Roll No. 102" required>{{ student_text }}</textarea>

                    <button type="submit">Send Attendance</button>
                </form>
            </div>

            <div class="panel summary">
                <h2>Attendance Summary</h2>
                <p><strong>College:</strong> {{ college_name }}</p>
                <p><strong>Class Time:</strong> {{ class_start }} - {{ class_end }}</p>
                <p><strong>Break Time:</strong> {{ break_start }} - {{ break_end }}</p>
                <p><strong>Student Message:</strong> {{ student_text }}</p>

                <div class="status">
                    Status: {{ status }}
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    form_values = get_form_values()
    status = "Waiting for attendance"

    if request.method == "POST":
        status = get_status(form_values["student_text"])

    return render_template_string(
        HTML,
        college_name=form_values["college_name"],
        class_start=form_values["class_start"],
        class_end=form_values["class_end"],
        break_start=form_values["break_start"],
        break_end=form_values["break_end"],
        student_text=form_values["student_text"],
        status=status,
    )


if __name__ == "__main__":
    app.run(debug=True)
