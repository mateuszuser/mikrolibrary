from app import app, db
from app.models import User, Book, Author, Avaible_notation

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "User": User,
       "Book": Book,
       "Author": Author,
       "Avaible_notation": Avaible_notation
   }