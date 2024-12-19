from flask import Flask
from routes import book_routes, member_routes

app = Flask(__name__)

app.register_blueprint(book_routes, url_prefix='/books')
app.register_blueprint(member_routes, url_prefix='/members')

@app.route('/')
def home():
    return "Welcome to the Library Management System!"

if __name__ == '__main__':
    app.run(debug=True)
