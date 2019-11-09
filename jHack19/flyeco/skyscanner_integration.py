import requests

default_market = "DE"
default_currency = "EUR"
default_locale = "EN-us"

base_url = "https://www.skyscanner.net/g/chiron/api/v1/"
default_header = {"api-key": "jacobs-2019"}
routes_url_ext = "flights/browse/browseroutes/v1.0/{}/{}/{}/".format(default_market, default_currency, default_locale)
place_url_ext = "places/autosuggest/v1.0/{}/{}/{}".format(default_market, default_currency, default_locale)

def get_place_id(query_str, value="PlaceId"):
    url = base_url+place_url_ext
    querystring = {"query":query_str}
    response = requests.request("GET", url, headers=default_header, params=querystring)
    if response.ok:
        return response.json().get("Places",[{}])[0].get(value, None).split("-")[0]
    return None

def get_routes(dest_id, depart_id, date_depart, date_return):
    url = base_url+routes_url_ext+"{}/{}/{}/{}".format(depart_id, dest_id, date_depart, date_return)
    response = requests.request("GET", url, headers=default_header)
    if response.ok:
        return response.json().get("Quotes",[{}])
    return {[]}

def handle_query(destination, departure, date_depart, date_return):
    dest_id = get_place_id(destination)
    depart_id = get_place_id(departure)
    dest_name = get_place_id(destination, "PlaceName")
    depart_name = get_place_id(departure, "PlaceName")
    if not dest_id or not depart_id:
        return [{}]
    retrieved = get_routes(dest_id, depart_id, date_depart, date_return)
    parsed = []
    for flight in retrieved:
        to_append = {}
        to_append["price"] = flight.get("MinPrice")
        to_append["from"] = depart_name
        to_append["to"] = dest_name
        parsed.append(to_append)

    return sorted(parsed, key = lambda i: i['price'])
    


    