from flask import Blueprint,render_template

contacts = Blueprint('contacts', __name__)

#ruta de inicio
@contacts.route("/")
def home():
    return render_template('index.html')

#ruta para nuevo contacto
@contacts.route('/new')
def add_contact():
    return "saving a contact"

@contacts.route("/update")
def update_contacts():
    return "update contact"

@contacts.route("/delete")
def deletec_contacts():
    return "delete contact"

@contacts.route("/about")
def about():
    return render_template('about.html')
