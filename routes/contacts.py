from flask import Blueprint,render_template,request,redirect
from models.contact import Contact #esto es el modelo
from utils.db import db #esta importacion es de la bd para poder usarla
contacts = Blueprint('contacts', __name__)

#ruta de inicio
@contacts.route("/")
def home():
    return render_template('index.html')

#ruta para nuevo contacto
@contacts.route('/new',methods=['POST'])
def add_contact():
    fullname=request.form['fullname']
    email= request.form['email']
    phone= request.form['phone']
    new_contact = Contact(fullname,email,phone)
    db.session.add(new_contact) #asi se guarda el contacto
    db.session.commit() #esto finaliza la consulta y lo guarda
    print(new_contact)
    return redirect('/')

@contacts.route("/update")
def update_contacts():
    return "update contact"

@contacts.route("/delete")
def deletec_contacts():
    return "delete contact"

@contacts.route("/about")
def about():
    return render_template('about.html')
