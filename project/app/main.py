from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Модель базы данных
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Пример данных для инициализации
@app.before_first_request
def create_tables():
    db.create_all()
    if not Item.query.first():  # Добавляем данные, если таблица пуста
        sample_items = [Item(name="Item 1"), Item(name="Item 2"), Item(name="Item 3")]
        db.session.add_all(sample_items)
        db.session.commit()

@app.route('/')
def index():
    items = Item.query.all()
    return render_template("index.html", items=items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
