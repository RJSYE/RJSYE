from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
migrate = Migrate(app,db)

db.init_app(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) #필수적으로 적어야 하는행(행번호를 나타냄)
    loginId= db.Column(db.String(20), nullable=False)
    password= db.Column(db.String(20), nullable=False)
    nickname= db.Column(db.String(20), nullable=False)

@app.route('/signup', methods =['POST', 'GET'])
def signup():
    if request.method=='POST':
        loginId = request.form['loginId']
        password = request.form['password']
        nickname = request.form['nickname']
        newuser = User(loginId=loginId, password=password, nickname=nickname)
        db.session.add(newuser)
        #Transaction이라는 개념이 적용됨
        db.session.commit()
    return render_template("signup.html")


if __name__ == '__main__':
    app.run()
