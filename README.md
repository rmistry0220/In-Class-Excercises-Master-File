# In-Class-Excercises-Master-File
## Setup

Create and activate a virtual environment (first time only):

```sh
conda create -n reports-env-2024 python=3.10
```

Activate the environment (whenever you come back to this):

```sh
conda activate reports-env-2024
```

Install packages
```sh
pip install -r requirements.txt
```

[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Create a ".env" file and add contents like the following (using your own AlphaVantage API Key):

```sh
# this is the ".env" file:
ALPHAVANTAGE_API_KEY="..."
```

## Usage

Run the unemployment script:

```sh
python app/unemployment.py

python -m app.unemployment

```

2
Run the stocks report:

```sh
python app/stocks.py

python -m app.stocks
```