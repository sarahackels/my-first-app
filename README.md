# my-first-app
My first app in opan 2023

Install packages:
```sh
    pip install -r requirements.txt
```


## Setup
Create and activate a virstual environemenmt:

```sh
    conda create -n my-first-env python=3.10
    
    conda activate my-first-env
``` 

Obtain an API Key from Alphavantage (https://www.alphavantage.co/support/#api-key) or from the professor ('ALPHAVANTAGE_API_KEY')

You must first follow the [setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md) to create an account, verify your account, setup a single sender, and obtain an API Key.

Create a ".env" file and paste in the following contents:

```sh
    ALPHAVANTAGE_API_KEY="______"
    SENDGRID_API_KEY="_________"
    SENDER_ADDRESS="name@gmail.com"
```


## Usage

Run the example script:
```sh
    python app/my_script.py 
```

Run the unemployment report:
```sh
    python -m app.unemployment
```

Send an example email:
```sh
    python app/email_service.py
```

Run enlarge function:
```sh
    python app/my_mod.py
```


Run stocks report:
```sh
    python -m app.stocks
```
Run weather function:
```sh
    python app/weather.py
```

Testing:
```sh
    pytest
```
### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file

    export FLASK_APP=web_app
    flask run
```


