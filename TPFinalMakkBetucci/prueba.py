from geopy.geocoders import Nominatim
 
# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")
 
 
# Latitude & Longitude input
Latitude = "-38.955628"
Longitude = "-68.062727"
 
location = geolocator.reverse(Latitude+","+Longitude)
 
address = location.raw['address']

city = address.get('state_district', '')
print(city)

