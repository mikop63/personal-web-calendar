from turtle import title
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

# создаем объект app
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
# в словаре находим ключ и присваем ему значение для подключения к БД
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
# постоянно отслеживает имзенения объектов. Откл для экномии памяти
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# создаем объект 'db' на основе класса SQLAlchemy а в конструктор
# передаем ему объект на основек класса Flask, где уже настроено поключение к нужной БД
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(2))
    month = db.Column(db.String(2))
    year = db.Column(db.String(4))
    color = db.Column(db.String(7), nullable=False)

    def __repr__(self):
        return f'<Articler {self.id}>'
#       выдается сам объект класса Articler и его ID
# создадим БД
# >>> from app import db; db.create_all(); exit()

@app.route('/')
@app.route('/home')
def home():

    return render_template('index.html')

@app.route('/add_event', methods=['POST', 'GET'])
def add_event():
    if request.method == 'POST':
        date = request.form['date'].split('-')
        color = request.form['color']

        # создаем объект на основе класса Article
        article = Article(day = date[2], month = date[1], year = date[0], color = color)

        # сохраняем этот объект в БД
        # try:
        print(date, '=',len(date))

        # добавляем созданный объект в БД
        db.session.add(article)
        # сохраняем объект
        db.session.commit()
        return redirect('/')
        
        # except:
        #     return 'при добавляение произошла ошибка'


    else: return render_template('add.html')


if __name__ == '__main__':
   app.run(debug=True,
            host='0.0.0.0',
            port=8080)
