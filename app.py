from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import PetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adoption_agency_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

### ROUTING ###
@app.route('/')
def show_homepage():
    """Display homepage."""

    pets = Pet.query.all()

    return render_template('base.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet_form():
    """Show new pet form, handle submission."""

    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('add-pet-form.html', form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_pet_details_and_edit_form(pet_id):
    """Show pet details and edit form, handle submission."""

    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')

    else:
        print("Errors:", form.errors)
        return render_template('pet-details.html', pet=pet, form=form)