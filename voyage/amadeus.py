from amadeus import Client, ResponseError

from django.conf import settings

amadeus = Client(
    client_id = settings.AMADEUS.get("API_KEY"),
    client_secret = settings.AMADEUS.get("API_SECRET")
)

print("Les valeurs ",amadeus)