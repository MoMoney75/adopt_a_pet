from flask import Flask, redirect,session,render_template,request
from forms import addPetForm
from models import db, connect_db, Pet

app = Flask(__name__)
app.app_context().push()
app.debug = True
app.config['SECRET_KEY'] = 'SEKRET'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ADOPT_A_PET'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True
connect_db(app)


@app.route('/')
def show_home_page():
    """shows home page with all current pets listed"""
    
    pets = Pet.query.all()

    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET','POST'])
def show_add_form():
    """gets form data for adding pet, creates instance of Pet if validated, else: returns user to form with form errors shown"""

    form = addPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url= form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name,species=species,photo_url=photo_url,age=age,notes=notes)
        db.session.add(pet)
        db.session.commit()

        return redirect('/')
    
    else:
        return render_template('add_pet.html', form=form)


@app.route('/<int:pet_id>/details', methods=['GET'])
def show_pet_details(pet_id):
    """shows additional details about the selected pet"""
   
    pet = Pet.query.get_or_404(pet_id)

    return render_template('pet_info.html', pet=pet)


@app.route('/<int:pet_id>/edit')
def show_pet_edit(pet_id):
    """renders form for editing a pet"""
    
    pet = Pet.query.get_or_404(pet_id)
    form = addPetForm(obj=pet)

    return render_template('edit_pet.html', pet=pet, form=form)

@app.route('/<int:pet_id>/edit/handle', methods=['GET','POST'])
def handle_pet_edit(pet_id):
    """handles form submission for editing the selected pet"""
   
    pet = Pet.query.get_or_404(pet_id)
    form = addPetForm()

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url= form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        
        db.session.commit()
    
        return redirect("/")
    
    else:
        return render_template('edit_pet.html')
    
@app.route('/<int:pet_id>/delete', methods=['GET','POST'])
def delete_pet(pet_id):
    """deletes the selected pet"""

    pet = Pet.query.get_or_404(pet_id)

    db.session.delete(pet)
    db.session.commit()

    return redirect('/')