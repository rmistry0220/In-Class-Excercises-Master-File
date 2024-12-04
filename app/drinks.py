import requests

def fetch_drinks():
    print("DRINKS...")
    
    api_url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic"
    response = requests.get(api_url)
    drinks_data = response.json().get("drinks", [])
    drinks = [
            {
                "name": drink.get("strDrink"),
                "image": drink.get("strDrinkThumb"),
                "id": drink.get("idDrink")
            }
            for drink in drinks_data[:20]
        ]
    
    return drinks
    
if __name__ == "__main__":
    data = fetch_drinks()
    print(data)
 