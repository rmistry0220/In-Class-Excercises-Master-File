from flask import Blueprint, render_template
import requests

# Create the Blueprint for drink routes
drink_routes = Blueprint("drink_routes", __name__)

@drink_routes.route("/drinks")
def drinks_list():
    print("DRINKS...")

    try:
        # Fetching data from the Cocktail DB API
        api_url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic"
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        drinks = response.json().get("drinks", [])
    except (requests.RequestException, ValueError) as e:
        print("Error fetching drinks data.")  # User-specified error message
        # Fallback data in case of an error
        drinks = [
            {
                "strDrink": "Mocktail",
                "strDrinkThumb": "https://via.placeholder.com/360x200.png?text=Mocktail",
                "idDrink": "0"
            }
        ]

    # Rendering the drinks template with the fetched or fallback data
    return render_template("drinks.html", drinks=drinks)

