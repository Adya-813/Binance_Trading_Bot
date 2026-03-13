from binance.client import Client

API_KEY = "dI10T4HWKNCpHXgfUQ2U8I25vhzsjwVQUGT0AXOWKgzDgNhGTmbzyJrtWigHRxO1"
API_SECRET = "OmUylQnfCPuYQ4mlKATEjC8JzaemDbbNL02C7NdbSONnK5BgpgIbyCL4NeG1uIXY"

def get_client():
    client = Client(API_KEY, API_SECRET, testnet=True)
    return client