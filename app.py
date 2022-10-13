from flask import Flask,render_template,request,redirect,flash,jsonify,Response
from models import db,ProductModel,SignupModel,CatModel,SubCatModel
from werkzeug.utils import secure_filename
import os
from wtforms import SelectField
from flask_wtf import FlaskForm

 
app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
UPLOAD_FOLDER = 'C:/Users/User/Desktop/assignment/static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/', methods=['GET','POST'])
def initial():
    if request.method == 'POST':
        email = request.form['email']
        role = request.form['role']
        password = request.form['password']
        u_id = SignupModel.query.filter_by(email=email).first()
        u_password = SignupModel.query.filter_by(password=password).first()
        u_role = SignupModel.query.filter_by(role=role).first()
        if not u_id or not u_password or not u_role:
            flash('Please check your login details and try again.')
            return redirect('/')
        else:
            if request.form['role'] == 'User':
                return redirect('/select')
            else:
                return redirect('/datalist')
    return render_template('login.html')
    
class Form(FlaskForm):
    category = SelectField('category', choices=[])
    subcategory = SelectField('subcategory', choices=[])


@app.route('/create' , methods = ['GET','POST'])
def create():
    form = Form()
    form.category.choices = [(cat.cat_id, cat.name) for cat in CatModel.query.all()]
    form.subcategory.choices = [(subcat.subcat_id, subcat.subcat_name) for subcat in SubCatModel.query.all()]
 
    if request.method == 'POST':
        first_name = request.form['first_name']
        cat_id = request.form['category']
        subcat_id = request.form['subcategory']
        p_description = request.form['p_description']
        p_type = request.form['p_type']
        p_price = request.form['p_price']
        file = request.files['photo']
        filename = secure_filename(file.filename)
        print("----------------------------------------")
        print(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("----------------------------------------")
        products = ProductModel(
            first_name=first_name,
            cat_id=cat_id,
            subcat_id=subcat_id,
            p_description=p_description,
            p_type= p_type,
            p_price=p_price,
            filename=filename
        )
        db.session.add(products)
        db.session.commit()
        return redirect('/datalist')
    return render_template('createpage.html',form=form )

@app.route('/subcategory/<get_subcategory>')
def subcatbycat(get_subcategory):
    subcategory = SubCatModel.query.filter_by(cat_id=get_subcategory).all()
    subcatArray = []
    for subcat in subcategory:
        subcatObj = {}
        subcatObj['id'] = subcat.subcat_id
        subcatObj['name'] = subcat.subcat_name
        subcatArray.append(subcatObj)
    return jsonify({'subcategory' : subcatArray})



@app.route('/addcategory' , methods = ['GET','POST'])
def cats():
    if request.method == 'GET':
        return render_template('AddCat.html')
 
    if request.method == 'POST':

        name = request.form['name']
        categorys = CatModel(
            name=name 
        ) 
        exists = CatModel.query.filter_by(name=name).all()
        if exists:
            flash('Category entered already exists.')
            return redirect('/addcategory')
        else:
            db.session.add(categorys)
            db.session.commit() 
        return redirect('/datalist')

@app.route('/addsub_category' , methods = ['GET','POST'])
def subcat():
    if request.method == 'GET':
        categorys =CatModel.query.all()
        subcategories =SubCatModel.query.all()
        return render_template('AddSubCat.html',categorys=categorys,subcategories=subcategories)
 
    if request.method == 'POST':
        subcat_name = request.form['subcat_name'] 
        cat_id = request.form['category']
        subcategories = SubCatModel(
            subcat_name=subcat_name,
            cat_id=cat_id
        )
        exists = SubCatModel.query.filter_by(subcat_name=subcat_name).all()
        if exists:
            flash('Sub-category entered already exists.')
            return redirect('/addsub_category')
        else:
            db.session.add(subcategories)
            db.session.commit()
        return redirect('/datalist')

@app.route('/datalist')
def RetrieveList():
    products =ProductModel.query.all()
    return render_template('datalist.html',products = products)

@app.route('/signup' , methods = ['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
 
    if request.method == 'POST':

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        phone = request.form['phone']
        role = request.form['role']
        file = request.files['photo']
        filename = secure_filename(file.filename)
        print("----------------------------------------")
        print(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("----------------------------------------")
        user = SignupModel.query.filter_by(email=email).first()
        if user:
            flash('Email address already exists')
            return redirect('/')
        signups = SignupModel(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            role=role,
            gender=gender, 
            phone = phone,
            filename=filename
        )
        db.session.add(signups)
        db.session.commit()
        return redirect('/')

class Form(FlaskForm):
    category = SelectField('category', choices=[])
    subcategory = SelectField('subcategory', choices=[])
    product = SelectField('product', choices=[])

@app.route('/select', methods=['GET', 'POST'])
def index():
    form = Form()
    form.category.choices = [(cat.cat_id, cat.name) for cat in CatModel.query.all()]
    form.subcategory.choices = [(subcat.subcat_id, subcat.subcat_name) for subcat in SubCatModel.query.all()]
    form.product.choices = [(product.prod_id, product.first_name) for product in ProductModel.query.all()]
    if request.method == 'POST':
       category = CatModel.query.filter_by(cat_id=form.category.data).first()
       subcategory = SubCatModel.query.filter_by(subcat_id=form.subcategory.data).first()
       product = ProductModel.query.filter_by(cat_id=form.category.data,subcat_id=form.subcategory.data).all()
       return render_template('viewprods.html',product=product)
    return render_template('select.html', form=form)

@app.route('/subcategory/<get_subcategory>')
def subbycat(get_subcategory):
    subcategory = SubCatModel.query.filter_by(cat_id=get_subcategory).all()
    subcatArray = []
    for subcat in subcategory:
        subcatObj = {}
        subcatObj['id'] = subcat.subcat_id
        subcatObj['name'] = subcat.subcat_name
        subcatArray.append(subcatObj)
    return jsonify({'subcategory' : subcatArray})
  
@app.route('/product/<get_product>')
def prodbycat(get_product):
    product = ProductModel.query.filter_by(subcat_id=get_product).all()
    productArray = []
    for prod in product:
        prodObj = {}
        prodObj['id'] = prod.prod_id
        prodObj['name'] = prod.first_name
        productArray.append(prodObj)
    return jsonify({'product' : productArray})

@app.route('/viewprods')
def user(cat_id,subcat_id):
    products = ProductModel.query.filter_by(cat_id=cat_id,subcat_id=subcat_id)
    categorys = CatModel.query.all()
    print(categorys)
    subcategories = SubCatModel.query.all()
    print(subcategories)
    return render_template('viewprods.html',products=products,categorys=categorys,subcategories=subcategories)
 
@app.route('/<int:id>')
def RetrieveEmployee(id):
    product = ProductModel.query.filter_by(id=id).first()
    if product:
        return render_template('data.html', product = product)
    return f"Employee with id ={id} Doenst exist"

@app.route('/<int:prod_id>/view',methods = ['GET','POST'])
def view(prod_id):
    product = ProductModel.query.filter_by(prod_id=prod_id).first()
    print("VALUES####",product)
    return render_template('view.html', product = product)
 
 
@app.route('/<int:prod_id>/edit',methods = ['GET','POST'])
def update(prod_id):
    product = ProductModel.query.filter_by(prod_id=prod_id).first()
    if request.method == 'POST':
        if product:
            db.session.delete(product)
            db.session.commit() 
        first_name = request.form['first_name']
        p_description = request.form['p_description']
        p_type = request.form['p_type']
        p_price = request.form['p_price']
        file = request.files['photo']
        filename = secure_filename(file.filename)
        print("----------------------------------------")
        print(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("----------------------------------------")

        product = ProductModel(
            first_name=first_name,
            p_description=p_description,
            p_type=p_type,
            p_price=p_price,
            filename=filename
        )
        db.session.add(product)
        db.session.commit()
        return redirect('/datalist')
    return render_template('update.html', product = product)
     

@app.route('/<int:prod_id>/delete', methods=['GET','POST'])
def delete(prod_id):
    product = ProductModel.query.filter_by(prod_id=prod_id).first()
    if request.method == 'POST':
        if product:
            db.session.delete(product)
            db.session.commit()
            return redirect('/datalist')
     #return redirect('/')
    return render_template('delete.html')

@app.route('/logout', methods=['GET','POST'])
def logout():
    return render_template('logout.html')
 
if __name__ == "__main__":
    app.run(debug=True)