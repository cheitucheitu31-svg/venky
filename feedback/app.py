from flask import Flask, render_template, request, redirect, url_for
from repository.feedback_repository import save_feedback

app = Flask(__name__)

@app.route("/", methods=["GET"])
def feedback_page():

    return render_template("feedback.html")

@app.route("/submit", methods=["POST"])
def submit_feedback():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # ✅ Basic validation
    if not name or not email or not message:
        return "All fields are required!", 400

    try:
        save_feedback(name, email, message)
    except Exception as e:
        return f"Error saving feedback: {str(e)}", 500

    return redirect(url_for("success_page"))

@app.route("/success")
def success_page():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
