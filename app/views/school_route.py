from flask import Blueprint, render_template, request, flash, redirect, url_for

school = Blueprint("school", __name__)


# HOME PAGE ROUTE (VIEW)
@school.get("/")
@school.get("/home")
def home_page():
    return render_template("index.html", title="Home | Brynno International School")


# ADMISSIONS PAGE ROUTE (VIEW)
@school.get("/admissions")
def admissions():
    return render_template("admissions.html", title="Admissions | Brynno International School")


# EVENTS PAGE ROUTE (VIEW)
@school.get("/events")
def events_page():
    return render_template("events.html", title="Events | Brynno International School")


# ABOUT PAGE ROUTE (VIEW)
@school.get("/about")
def about_page():
    return render_template("about.html", title="About | Brynno International School")



# CONTACT PAGE ROUTE (VIEW)
@school.get("/contact")
def contact_page():
    return render_template("contact.html", title="Contact | Brynno International School")


# PROPRIETRESS PAGE ROUTE (VIEW)
@school.get("/proprietress")
def proprietress_page():
    return render_template("proprietress.html", title="Proprietress | Brynno International School")


# CRECHE PAGE ROUTE (VIEW)
@school.get("/crèche")
def creche_page():
    return render_template("crèche.html", title="Crèche | Brynno International School")
