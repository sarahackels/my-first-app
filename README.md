# my-first-app
my first app in opan 2023

install packages:
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

create a ".env" file and paste in the following contents:

```sh
    ALPHAVANTAGE_API_KEY="______"
```


## Usage

Run the example script:
```sh
    python app/my_script.py 
```

Run the unemployment report:
```sh
    python app/unemployment.py
```

