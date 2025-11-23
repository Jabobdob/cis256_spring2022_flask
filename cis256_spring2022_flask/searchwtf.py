from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from booksdb import BooksDB

class SearchWTF(FlaskForm):
    myoptions = [(None, "Choose your Search Type"), ('byAuthor','By Author'),('byTitle','By Title'),
                 ('byPublisher','By Publisher')]
    search_choice = SelectField("SearchChoice", choices=myoptions,validators=[DataRequired()] )

class ByAuthorIdWTF(FlaskForm):
    mydb = BooksDB()
    authors = mydb.getauthors()
    author_choice = SelectField("AuthorChoice", choices=authors)


# this is for picking a publisher. similar to the author one
class ByPublisherIdWTF(FlaskForm):
    publisher_choice = SelectField("Pick a Publisher:", choices=[], coerce=int)
    submit = SubmitField("Go")

class ByTitleWTF(FlaskForm):
    # just a simple text box for typing part of a title
    title_string = StringField("Enter Part of a Title:")
    submit = SubmitField("Search")

