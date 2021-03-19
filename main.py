import phonenumbers 
from test import number
from phonenumbers import geocoder, carrier

ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en"), "\nNote: If this is a US phone number the above result could be a state.")
