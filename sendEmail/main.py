from flask import Flask, render_template,request
import smtplib
import requests

# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
OWN_EMAIL = "suresh.doddi@techolution.com"
OWN_PASSWORD = "bfec rpjm wvdn nisc"

appPass = "bfec rpjm wvdn nisc"

app = Flask(__name__)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def login():
    name = request.form['username']
    password = request.form['password']
    return f"<h1>user name : {name} \n password : {password}</h1>"


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/sendEmail", methods=['POST'])
def sendEmail():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(OWN_EMAIL, OWN_PASSWORD)
            connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)
            # Move the quit() call inside the with block
            connection.quit()
    except smtplib.SMTPAuthenticationError as e:
        print(f"Authentication failed. Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == '__main__':
    app.run(debug=True)
