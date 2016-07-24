from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")
    #this should be homepage, fix this and it should work

    return render_template("index.html")

@app.route("/application-form")
def job_application():
    """Show the job application form."""


    return render_template("application-form.html")

@app.route("/application", methods=['POST'])
def thank_response():
    """acknowledges the user's application"""
    #.title() capitalized the first letter in the str
    first = request.form.get("firstname").title()
    last = request.form.get("lastname").title()
    salary = request.form.get("salaryreq")
    position = request.form.get("job")

    return render_template("application-response.html", first=first, last=last,
        salary=salary, position=position)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
