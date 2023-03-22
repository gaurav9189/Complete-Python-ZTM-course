from flask import Flask, render_template, request, redirect
from markupsafe import escape
import csv
app = Flask(__name__)
print(__name__)


@app.route("/")
def home():
    # return "<p>Hello, World!</p>"
    return render_template('index.html')


@app.route("/<page_name>")
def my_home(page_name):
    # return "<p>Hello, World!</p>"
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        database_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong'


# def database_write(data):
#     with open('database.txt', 'a') as db:
#         for k, v in data.items():
#             db.write(f'{k}: {v}\n')


def database_csv(data):
    with open('database.csv', 'a') as db1:
        csvwriter = csv.writer(db1, delimiter=',', quotechar=' ')
        email = data['email']
        subject = data['subject']
        message = data['message']
        csvwriter.writerow([email, subject, message])
