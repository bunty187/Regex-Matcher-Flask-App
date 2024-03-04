from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "test_string" in request.form:
            test_string = request.form["test_string"]
            regex = request.form["regex"]
            matched_strings = re.findall(regex, test_string)
            return render_template("results.html", test_string=test_string, regex=regex, matched_strings=matched_strings)
    return render_template("index.html")


@app.route('/email_validation', methods=['GET', 'POST'])
def email_validation():
    if request.method == 'POST':
        if "email_string" in request.form:
            email_string = request.form.get('email_string')
            # Regex pattern for email validation
            # pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
            email_list = email_string.split(',')
            valid_emails = []
            invalid_emails = []
            for email in email_list:
                email = email.strip()
                if re.match(pattern, email):
                    valid_emails.append(email)
                else:
                    invalid_emails.append(email)
            return render_template('email_validation.html', valid_emails=valid_emails, invalid_emails=invalid_emails)
    return render_template('email_validation.html')


if __name__ == "__main__":
    app.run(debug=True)
