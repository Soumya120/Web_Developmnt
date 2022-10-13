from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


db =SQLAlchemy()
class SignupModel(UserMixin,db.Model):
    __tablename__ = "signups"
 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    gender = db.Column(db.String())
    phone = db.Column(db.String())
    role = db.Column(db.String())
    filename = db.Column(db.String())

 
    def __init__(self, first_name,last_name,email,password,
                gender,phone,role,filename):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.gender = gender
        self.phone = phone 
        self.role = role
        self.filename = filename
 
    def __repr__(self):
        return f"{self.last_name}"

class CatModel(db.Model):
    __tablename__ = "categorys"
    __table_args__ = {'extend_existing': True}

    cat_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    def __repr__(self):
        return '\n cat_id:  name: '.format(self.cat_id, self.name)
    
    def __str__(self):

        return '\n cat_id:  name: '.format(self.cat_id, self.name)

class SubCatModel(db.Model):
    __tablename__ = "subcategories"
    __table_args__ = {'extend_existing': True}

    subcat_id = db.Column(db.Integer, primary_key=True)
    cat_id = db.Column(db.Integer, db.ForeignKey('categorys.cat_id'))
    subcat_name = db.Column(db.String()) 
    def __repr__(self):
    
        return '\n subcat_id:  cat_id:  subcat_name: '.format(self.subcat_id, self.cat_id, self.subcat_name)


    def __str__(self):

        return '\n subcat_id:  cat_id:  subcat_name: '.format(self.subcat_id, self.cat_id, self.subcat_name)

class ProductModel(db.Model):
    __tablename__ = "products"
    __table_args__ = {'extend_existing': True}

    prod_id = db.Column(db.Integer, primary_key=True)
    subcat_id = db.Column(db.Integer, db.ForeignKey('subcategories.subcat_id'))
    cat_id = db.Column(db.Integer, db.ForeignKey('categorys.cat_id'))
    first_name = db.Column(db.String())
    p_description = db.Column(db.String())
    p_price = db.Column(db.String())
    p_type = db.Column(db.String())
    filename=db.Column(db.String())

    def __repr__(self):
    
        return '\n prod_id:  first_name:  p_description:  p_price:  p_type:  subcat_id:  cat_id:  '.format(self.prod_id,  self.first_name,  self.p_description,  self.p_price,  self.p_type,  self.subcat_id,  self.cat_id)


    def __str__(self):

        return '\n prod_id:  first_name:  p_description:  p_price:  p_type:  subcat_id:  cat_id:  '.format(self.prod_id,  self.first_name,  self.p_description,  self.p_price,  self.p_type,  self.subcat_id,  self.cat_id)

