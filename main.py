import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

number =input("Enter your Phone number with Nation code :-")

ch_number = phonenumbers.parse(number, "CH")
country = geocoder.description_for_number(ch_number, "en")
# country = geocoder.description_for_valid_number(ch_number, "en")
# country = geocoder.country_name_for_number(ch_number, "en")


service_number = phonenumbers.parse(number, "RO")
service_provider = carrier.name_for_number(service_number, "en")
# service_provider = carrier.name_for_valid_number(service_number, "en")

gb_number = phonenumbers.parse(number, "GB")
tz = timezone.time_zones_for_number(gb_number)[0]
# tz = timezone.time_zones_for_geographical_number(gb_number)

print("country :-",country)
print("service_provider :-",service_provider)
print("time-zone:-",tz)
