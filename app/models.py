from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    email = db.Column(db.String(200), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    avaible = db.relationship("Avaible_notation", backref="customer", lazy="dynamic")

    def __str__(self):
       return f"<User {self.username}>"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    authors = db.relationship("Author", backref="author", lazy="dynamic")
    avaible = db.relationship("Avaible_notation", backref="borrow_book", lazy="dynamic")

    def __str__(self):
        return f"<Book {self.id} {self.name[:50]} ...>"

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f"<Author {self.id} {self.body[:50]} ...>"

class Avaible_notation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    borrow_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    give_back_date = db.Column(db.DateTime, index=True, default=None)
    def give_back_the_book():
        give_back_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __str__(self):

        return f"<Avaible_notation {self.id} User ID{self.user_id} Book ID {self.book_id}>"