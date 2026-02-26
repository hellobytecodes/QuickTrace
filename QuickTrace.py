from phonenumbers import carrier, geocoder, timezone
from os import system
from time import sleep
import phonenumbers
import requests
import json

RED_BOLD = "\033[1;31m"
GREEN_BOLD = "\033[1;32m"
YELLOW_BOLD = "\033[1;33m"
BLUE_BOLD = "\033[1;34m"
MAGENTA_BOLD = "\033[1;35m"
CYAN_BOLD = "\033[1;36m"
WHITE_BOLD = "\033[1;37m"

system("clear" or "cls")

bnr = GREEN_BOLD+"""
                      _.....__
                     (.--...._`'--._
           _,...----''''`-.._ `-..__`.._
  __.--'-;..-------'''''`._')      `--.-.__
'-------------------------------------------'
\ '----------------  ,-.  .-------------'. |
 \`.              ,','  \ \             ,' /
  \ \             / /   `.`.          ,' ,'
  `. `.__________/,'     `.' .......-' ,'
    `............-'        "---------''
"""
print(bnr)
print()

print(GREEN_BOLD+"[1] Number Tracker")
print(GREEN_BOLD+"[2] IP Tracker")
print(GREEN_BOLD+"[3] Exit")
num = input(CYAN_BOLD+"Enter Your Number: ")

if num == "1":
  print()
  phone = input(YELLOW_BOLD+"Enter The Phonenumber code (e.g +9893600000): "+WHITE_BOLD)
  number = phonenumbers.parse(phone, None)
  sleep(2)
  location = geocoder.country_name_for_number(number, "en")
  region = geocoder.description_for_number(number, "en")
  tz = timezone.time_zones_for_number(number)[0]
  operator = carrier.name_for_number(number, "en")
  valid = phonenumbers.is_valid_number(number)
  possible = phonenumbers.is_possible_number(number)
  intl = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
  e164 = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)
  local = number.national_number
  print(GREEN_BOLD+"=" * 50)
  print(GREEN_BOLD+f"Location             : {location}")
  print(GREEN_BOLD+f"Region Code          : {region}")
  print(f"Timezone             : {tz}")
  print(GREEN_BOLD+f"Operator             : {operator}")
  print(GREEN_BOLD+f"Valid number         : {valid}")
  print(GREEN_BOLD+f"Possible number      : {possible}")
  print(GREEN_BOLD+f"International format : {intl}")
  print(GREEN_BOLD+f"Mobile format        : {intl}")
  print(GREEN_BOLD+f"Original number      : {local}")
  print(GREEN_BOLD+f"E.164 format         : {e164}")
  print(GREEN_BOLD+f"Country code         : +{number.country_code}")
  print(GREEN_BOLD+f"Local number         : {local}")
  print(GREEN_BOLD+"=" * 50)
  
elif num == "2":
    print()
    ip = input(YELLOW_BOLD + "Enter The IP (e.g 5.125.0.1): " + WHITE_BOLD)
    print()
    print(GREEN_BOLD + "Show Information IP Address")
    
    req_api = requests.get(f"http://ipwho.is/{ip}")
    ip_data = json.loads(req_api.text)
    
    sleep(2)
    
    print(f"{GREEN_BOLD}\n IP target       :{YELLOW_BOLD}", ip)
    print(f"{GREEN_BOLD} Type IP         :{YELLOW_BOLD}", ip_data.get("type", "N/A"))
    print(f"{GREEN_BOLD} Country         :{YELLOW_BOLD}", ip_data.get("country", "N/A"))
    print(f"{GREEN_BOLD} Country Code    :{YELLOW_BOLD}", ip_data.get("country_code", "N/A"))
    print(f"{GREEN_BOLD} City            :{YELLOW_BOLD}", ip_data.get("city", "N/A"))
    print(f"{GREEN_BOLD} Continent       :{YELLOW_BOLD}", ip_data.get("continent", "N/A"))
    print(f"{GREEN_BOLD} Continent Code  :{YELLOW_BOLD}", ip_data.get("continent_code", "N/A"))
    print(f"{GREEN_BOLD} Region          :{YELLOW_BOLD}", ip_data.get("region", "N/A"))
    print(f"{GREEN_BOLD} Region Code     :{YELLOW_BOLD}", ip_data.get("region_code", "N/A"))
    print(f"{GREEN_BOLD} Latitude        :{YELLOW_BOLD}", ip_data.get("latitude", "N/A"))
    print(f"{GREEN_BOLD} Longitude       :{YELLOW_BOLD}", ip_data.get("longitude", "N/A"))
    
    lat = int(ip_data.get('latitude', 0))
    lon = int(ip_data.get('longitude', 0))
    
    print(f"{GREEN_BOLD} Maps            :{YELLOW_BOLD}", f"https://www.google.com/maps/@{lat},{lon},15z")
    print(f"{GREEN_BOLD} EU              :{YELLOW_BOLD}", ip_data.get("is_eu", "N/A"))
    print(f"{GREEN_BOLD} Postal          :{YELLOW_BOLD}", ip_data.get("postal", "N/A"))
    print(f"{GREEN_BOLD} Calling Code    :{YELLOW_BOLD}", ip_data.get("calling_code", "N/A"))
    print(f"{GREEN_BOLD} Capital         :{YELLOW_BOLD}", ip_data.get("capital", "N/A"))
    print(f"{GREEN_BOLD} Borders         :{YELLOW_BOLD}", ip_data.get("borders", "N/A"))
    
    # Flag
    if "flag" in ip_data:
        print(f"{GREEN_BOLD} Country Flag    :{YELLOW_BOLD}", ip_data["flag"].get("emoji", "N/A"))
    
    # Connection
    if "connection" in ip_data:
        conn = ip_data["connection"]
        print(f"{GREEN_BOLD} ASN             :{YELLOW_BOLD}", conn.get("asn", "N/A"))
        print(f"{GREEN_BOLD} ORG             :{YELLOW_BOLD}", conn.get("org", "N/A"))
        print(f"{GREEN_BOLD} ISP             :{YELLOW_BOLD}", conn.get("isp", "N/A"))
        print(f"{GREEN_BOLD} Domain          :{YELLOW_BOLD}", conn.get("domain", "N/A"))
    
    # Timezone
    if "timezone" in ip_data:
        tz_data = ip_data["timezone"]
        print(f"{GREEN_BOLD} ID              :{YELLOW_BOLD}", tz_data.get("id", "N/A"))
        print(f"{GREEN_BOLD} ABBR            :{YELLOW_BOLD}", tz_data.get("abbr", "N/A"))
        print(f"{GREEN_BOLD} DST             :{YELLOW_BOLD}", tz_data.get("is_dst", "N/A"))
        print(f"{GREEN_BOLD} Offset          :{YELLOW_BOLD}", tz_data.get("offset", "N/A"))
        print(f"{GREEN_BOLD} UTC             :{YELLOW_BOLD}", tz_data.get("utc", "N/A"))
elif num == "3":
    exit()
else:
  print(RED_BOLD+"Type Error !")