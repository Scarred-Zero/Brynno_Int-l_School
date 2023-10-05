from flask import Blueprint, render_template, request, flash, redirect, url_for

school = Blueprint("school", __name__)


# HOME PAGE ROUTE (VIEW)
@school.get("/")
@school.get("/home")
def home_page():
    return render_template("index.html", title="Home | Brynno Int'l School")


# ADMISSIONS PAGE ROUTE (VIEW)
@school.get("/admissions")
def admissions():
    return render_template("admissions.html", title="Admissions | Brynno Int'l School")


# EVENTS PAGE ROUTE (VIEW)
@school.get("/events")
def events_page():
    return render_template("events.html", title="Events | Brynno Int'l School")


# ABOUT PAGE ROUTE (VIEW)
@school.get("/about")
def about_page():
    return render_template("about.html", title="About | Brynno Int'l School")


# CONTACT PAGE ROUTE (VIEW)
@school.get("/contact")
def contact_page():
    return render_template("contact.html", title="Contact | Brynno Int'l School")


# PROPRIETRESS PAGE ROUTE (VIEW)
@school.get("/proprietress_page")
def proprietress_page():
    return render_template("proprietress.html", title="Proprietress | Brynno Int'l School")


# SCHOOL ROUTES
# CRECHE PAGE ROUTE (VIEW)
@school.get("/crèche_site")
def creche_page():
    return render_template("crèche.html", title="Crèche | Brynno Int'l School")


# NURSERY PAGE ROUTE (VIEW)
@school.get("/nursery_site")
def nursery_page():
    return render_template("nursery.html", title="Nursery | Brynno Int'l School")


# PRIMARY PAGE ROUTE (VIEW)
@school.get("/primary_site")
def primary_page():
    return render_template("primary.html", title="Primary | Brynno Int'l School")


# SECONDARY PAGE ROUTE (VIEW)
@school.get("/secondary_site")
def secondary_page():
    return render_template("secondary.html", title="Secondary | Brynno Int'l School")
