from hue_api import HueApi

api = HueApi()

api.load_existing()

api.fetch_lights()

print(api.lights)