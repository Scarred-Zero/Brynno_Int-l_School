from flask import Blueprint, render_template, request, flash, redirect, session
from ..config.database import get_connection
from werkzeug.security import generate_password_hash, check_password_hash
from ..utils.decorators import authenticated_admin, guest_admin, prevent_multiple

admin = Blueprint("admin", __name__)

db = get_connection()


# LOGIN ROUTE (VIEW)
@admin.get("/login")
@guest_admin
def login_page():
    return render_template("admin/login.html")


# HANDLE ADMIN LOGIN
@admin.post("/login")
def handle_login_admin():
    form = request.form
    # FROM FIELDS
    email = form.get("email")
    password = form.get("password")

    if not db:
        flash("Error connecting to db", "danger")
        return redirect("/admin")

    conn, cursor = db

    # GET THE ADMIN
    query = "SELECT * FROM admin WHERE email = %s"
    cursor.execute(query, [email])

    admin = cursor.fetchone()

    if not admin:
        flash("Admin does not exist", "danger")
        return redirect("/admin")

    # VERIFY THE PASSWORD
    if not check_password_hash(admin.get("password"), password):
        flash("Incorrect credentials", "danger")
        return redirect("/admin")

    # CREATE ADMIN LOGIN SESSION
    session["ADMIN_LOGIN"] = admin.get("email")
    session["ADMIN_NAME"] = admin.get("name")

    flash("Login successful!", "success")
    return redirect("/admin/dashboard")


# HANDLE ADMIN LOGOUT
@admin.get("/logout")
def logout_admin():
    session.pop("ADMIN_LOGIN", None)
    return redirect("/admin/login")


# REGISTER ROUTE (VIEW)
@admin.get("/register")
@admin.get("/sign-up")
@guest_admin
@prevent_multiple
def register_page():
    return render_template("admin/register.html")


# HANDLE ADMIN REGISTER
@admin.post("/create")
def handle_register_admin():
    form = request.form
    # GET THE FORM FIELDS
    name = form.get("name")
    email = form.get("email")
    password = form.get("password")
    hashed_password = generate_password_hash(password)

    if not db:
        flash("Error connecting to db", "danger")
        return redirect("/admin/register")

    conn, cursor = db
    query = "INSERT INTO admin(name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, [name, email, hashed_password])
    conn.commit()

    if not cursor.rowcount:
        flash("Failed to register admin", "danger")
        return redirect("/admin/register")

    flash("Registration successful!", "success")
    return redirect("/admin")


# DASHBOARD PAGE (VIEW)
@admin.get("/dashboard")
@authenticated_admin
def dashboard_page():
    if not db:
        flash("Failed to connect to db", "danger")
        return redirect("/admin/dashboard")

    return render_template("admin/dashboard.html")

