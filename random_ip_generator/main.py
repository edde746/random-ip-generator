import csv
import random
import ipaddress

ip_ranges = []
reader = csv.reader(open("IP2LOCATION-LITE-DB1.CSV").read().strip().split('\n'))
for row in reader:
    ip_ranges.append((int(row[0]), int(row[1]), row[2], row[3]))

def filter_ranges_by_country(ip_ranges, country_code):
    return [ip_range for ip_range in ip_ranges if ip_range[2] == country_code]

def random_ip_for_country(country_code):
    global ip_ranges
    filtered_ranges = filter_ranges_by_country(ip_ranges, country_code)

    if not filtered_ranges:
        raise ValueError(f"No IP ranges found for country code: {country_code}")

    selected_range = random.choice(filtered_ranges)
    random_ip = random.randint(selected_range[0], selected_range[1])

    return ipaddress.IPv4Address(random_ip)
