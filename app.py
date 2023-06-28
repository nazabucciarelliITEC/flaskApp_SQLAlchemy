from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import ForeignKey

app = Flask(__name__)

# estructura de uri de sql = mysql+pymysql://usuario:contraseña@ip/nombre_db

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@127.0.0.1/db_local_bucciarelli_alchemy"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Country(db.Model):
    __tablename__ = "country"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return self.name


class Province(db.Model):
    __tablename__ = "province"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.Integer, ForeignKey(
        "country.id"), nullable=False)
 
    def __str__(self):
        return self.name


class Locality(db.Model):
    __tablename__ = "locality"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    province_id = db.Column(db.Integer, ForeignKey(
        "province.id"), nullable=False)

    def __str__():
        return self.name


class Person(db.Model):
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    locality = db.Column(db.Integer,ForeignKey("locality.id"),nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    isActive = db.Column(db.Boolean, nullable=False,default=True)

    def __str__():
        return self.name + " " + self.lastname

 
@app.context_processor  
def inject_countries():
    countries = db.session.query(Country).all() 
    return dict(countries = countries) # Se usa el dict() porque es mas legible. Lo parsea a dictionarie
 
@app.route("/")
def index():
    return render_template("index.html")
  
@app.route("/add_country", methods=['POST'])
def add_country():
    if request.method == 'POST':
        country_name = request.form['name']
        new_country = Country(name=country_name)
        db.session.add(new_country)
        db.session.commit()
        return redirect(url_for('index'))   
                       
@app.route("/delete_country/<id>")
def delete_country(id):
    country = Country.query.get(id)
    db.session.delete(country)
    db.session.commit()
    return redirect(url_for('index')) 
     
  