

##imports at the top of the file

from IPython.display import Image, display
from IPython.core.display import HTML
import pgeocode
from pgeocode import Nominatim
import requests
import json
from pandas import DataFrame


def display_forecast(zip_code, country_code="US"):
    """
    Displays a seven day weather forecast for the provided zip code.

    Params :

        country_code (str) a valid country code (see supported country codes list). Default is "US".

        zip_code (str) a valid US zip code, like "20057" or "06510".

    """

    nomi = Nominatim(country_code)
    geo = nomi.query_postal_code(zip_code)
    latitude = geo["latitude"]
    longitude = geo["longitude"]

    request_url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(request_url)
    #print(response.status_code)
    parsed_response = json.loads(response.text)

    forecast_url = parsed_response["properties"]["forecast"]
    forecast_response = requests.get(forecast_url)
    #print(forecast_response.status_code)
    parsed_forecast_response = json.loads(forecast_response.text)

    periods = parsed_forecast_response["properties"]["periods"]
    daytime_periods = [period for period in periods if period["isDaytime"] == True]

    for period in daytime_periods:
        #print(period.keys())
        print("-------------")
        print(period["name"], period["startTime"][0:7])
        print(period["shortForecast"], f"{period['temperature']} {DEGREE_SIGN}{period['temperatureUnit']}")
        #print(period["detailedForecast"])
        display(Image(url=period["icon"]))


def to_image(url):
    return '<img src="'+ url + '" width="32" >'


def chopped_date(start_time):
    return start_time[5:10]


def forecast_demo(zip_code, country_code="US"):
    """
    Displays a seven day weather forecast for the provided zip code.

    Params :

        country_code (str) a valid country code (see supported country codes list). Default is "US".

        zip_code (str) a valid US zip code, like "20057" or "06510".

    """
    nomi = Nominatim(country_code)
    geo = nomi.query_postal_code(zip_code)
    latitude = geo["latitude"]
    longitude = geo["longitude"]

    request_url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(request_url)
    #print(response.status_code)
    parsed_response = json.loads(response.text)

    forecast_url = parsed_response["properties"]["forecast"]
    forecast_response = requests.get(forecast_url)
    #print(forecast_response.status_code)
    parsed_forecast_response = json.loads(forecast_response.text)

    periods = parsed_forecast_response["properties"]["periods"]
    daytime_periods = [period for period in periods if period["isDaytime"] == True]

    #for period in daytime_periods:
    #    #print(period.keys())
    #    print("-------------")
    #    print(period["name"], period["startTime"][0:7])
    #    print(period["shortForecast"], f"{period['temperature']} {DEGREE_SIGN}{period['temperatureUnit']}")
    #    #print(period["detailedForecast"])
    #    display(Image(url=period["icon"]))


    df = DataFrame(daytime_periods)

    df["date"] = df["startTime"].apply(chopped_date)

    # df["img"] = df["icon"].apply(to_image)

    # combined column for temp display
    # ... h/t: https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-pandas-dataframe
    df["temp"] = df["temperature"].astype(str) + " " + DEGREE_SIGN + df["temperatureUnit"]

    # rename cols:
    df.rename(columns={
        "name":"day",
        "shortForecast": "forecast"
    }, inplace=True)

    # drop unused cols:
    df.drop(columns=[
        "temperature", "temperatureUnit", "temperatureTrend",
        "windSpeed", "windDirection",
        "startTime", "endTime",
        "number", "isDaytime", "detailedForecast"
    ], inplace=True)

    # re-order columns:
    df = df.reindex(columns=['day', 'date', 'temp', 'forecast', 'icon'])

    # return df
    print("---")
    print("SEVEN DAY FORECAST")
    print("LOCATION:", f"{geo.place_name}, {geo.state_code}".upper())
    print("---")
    return HTML(df.to_html(escape=False, formatters=dict(icon=to_image)))


## one way that I refactored the function.
def header():
    print("-----------")

if __name__ == "__main__":
    header()
    print("EXAMPLE IMAGES:")

    header()
    image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Georgetown_Hoyas_logo.svg/64px-Georgetown_Hoyas_logo.svg.png"
    display(Image(url=image_url))

    header()
    display(Image(url="https://www.python.org/static/community_logos/python-powered-w-200x80.png"))

    header()
    display(Image(url="https://api.weather.gov/icons/land/day/sct?size=medium"))


    DEGREE_SIGN = u"\N{DEGREE SIGN}"
    print(f"THE TEMPERATURE IS 90 {DEGREE_SIGN}F")


    nomi = pgeocode.Nominatim('US')
    results = nomi.query_postal_code("20057")

    print(results)
    print(type(results))

    print("LOCATION:", f"{results['place_name']}, {results['state_code']}")
    print("LAT:", results["latitude"])
    print("LON:", results["longitude"])

    zip_code = input("Please input a zip code (e.g. '06510'): ") or "06510"
    print("ZIP CODE:", zip_code)

    nomi = Nominatim('US')
    geo = nomi.query_postal_code(zip_code)
    print("LOCATION INFO:")
    print(geo)

    latitude = geo["latitude"]
    longitude = geo["longitude"]

    request_url = f"https://api.weather.gov/points/{latitude},{longitude}"
    print(request_url)
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)

    print(response.status_code)

    forecast_url = parsed_response["properties"]["forecast"]
    print(forecast_url)

    forecast_response = requests.get(forecast_url)
    parsed_forecast_response = json.loads(forecast_response.text)
    #parsed_forecast_response

    periods = parsed_forecast_response["properties"]["periods"]
    #print(len(periods))

    daytime_periods = [period for period in periods if period["isDaytime"] == True]
    #print(len(daytime_periods))

    for period in daytime_periods:
        #print(period.keys())
        print("-------------")
        print(period["name"], period["startTime"][0:7])
        print(period["shortForecast"], f"{period['temperature']} {DEGREE_SIGN}{period['temperatureUnit']}")
        #print(period["detailedForecast"])
        display(Image(url=period["icon"]))
    
    my_zip = '20057'
    display_forecast(my_zip)
    forecast_demo("06070")