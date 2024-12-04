#drink_routes.py

from flask import Blueprint, render_template, redirect
import requests
from app.drinks import fetch_drinks

drink_routes = Blueprint("drink_routes", __name__)

@drink_routes.route("/drinks")
def drinks_list():
    print("DRINKS...")
    try:
        drinks = fetch_drinks()
        #print(drinks)
        return render_template("drinks.html", drinks=drinks[:20])
    except Exception as err:
        print('OOPS', err)
        #flash("Market Data Error. Please check your symbol and try again!", "danger")
        return redirect("/")


