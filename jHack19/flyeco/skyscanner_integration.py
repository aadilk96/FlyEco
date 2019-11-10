import requests

default_market = "DE"
default_currency = "EUR"
default_locale = "EN-us"

base_url = "https://www.skyscanner.net/g/chiron/api/v1/"
default_header = {"api-key": "jacobs-2019"}
routes_url_ext = "flights/browse/browseroutes/v1.0/{}/{}/{}/".format(default_market, default_currency, default_locale)
place_url_ext = "places/autosuggest/v1.0/{}/{}/{}".format(default_market, default_currency, default_locale)
eco_url_ext = "eco/average-emissions"

def get_place_id(query_str, value="PlaceId"):
    url = base_url+place_url_ext
    querystring = {"query":query_str}
    response = requests.request("GET", url, headers=default_header, params=querystring)
    if len(response.json().get("Places",[{}])) == 0:
        return None
    first = response.json().get("Places",[{}])[0].get(value, None).split("-")[0]
    if len(first) < 4:
        return first
    if len(response.json().get("Places",[{}])) > 1:
        second = response.json().get("Places",[{}])[1].get(value, None).split("-")[0]
        if len(second) < 4:
            return second
    if len(response.json().get("Places",[{}])) > 2:
        third = response.json().get("Places",[{}])[2].get(value, None).split("-")[0]
        if len(third) < 4:
            return third
    return None

def get_routes(dest_id, depart_id, date_depart, date_return):
    url = base_url+routes_url_ext+"{}/{}/{}/{}".format(depart_id, dest_id, date_depart, date_return)
    response = requests.request("GET", url, headers=default_header)
    print("the url is", url)
    if response.ok:
        return response.json().get("Quotes",[{}])

    return [{}]

def get_emissions(dest_id, depart_id):
    url = base_url+eco_url_ext
    querystring = {"routes": depart_id+","+dest_id}
    response = requests.request("GET", url, headers=default_header, params=querystring)
    print("the response is", response.text)
    if response.ok:
        return response.json()[0].get("perSeatEmissions")

    return ""


def handle_query(destination, departure, date_depart, date_return):
    print("handle_query called with", destination, departure, date_depart, date_return)
    dest_id = get_place_id(destination)
    depart_id = get_place_id(departure)
    dest_name = get_place_id(destination, "PlaceName")
    depart_name = get_place_id(departure, "PlaceName")
    print("Places are", dest_id, depart_id, dest_name, depart_name)
    if not dest_id or not depart_id:
        return [{}]
    retrieved = get_routes(dest_id, depart_id, date_depart, date_return)
    carbon = get_emissions(dest_id, depart_id)
    parsed = []
    for flight in retrieved:
        to_append = {}
        to_append["price"] = int(flight.get("MinPrice"))
        to_append["from"] = depart_name
        to_append["to"] = dest_name
        to_append["depart_date"] = flight.get("OutboundLeg", {}).get("DepartureDate", "").split("T")[0]
        to_append["return_date"] = flight.get("InboundLeg", {}).get("DepartureDate", "").split("T")[0]
        to_append["carbon"] = carbon
        parsed.append(to_append)
    print("about to return", parsed)
    return sorted(parsed, key = lambda i: i['price'])
    


    