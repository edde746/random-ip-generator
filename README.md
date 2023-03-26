# Random IP Generator

Random IP Generator is a Python package that generates a random IP address for a given country code. It uses the IP2LOCATION-LITE-DB1.CSV file as a source for IP ranges per country.

## Installation
You can install the package via pip:

```bash
pip install random-ip-generator
```

##Usage
After installing the package, you can use the `random_ip_for_country` function in your Python script to generate a random IP address for a given country.

```python
from random_ip_generator import random_ip_for_country

country_code = "US"
random_ip = random_ip_for_country(country_code)
print(f"Random IP for {country_code}: {random_ip}")
```

## Prerequisites
This package requires the `ipaddress` package. It will be installed automatically if you install `random-ip-generator` via pip.

## Attribution

This site or product includes IP2Location LITE data available from [https://lite.ip2location.com](https://lite.ip2location.com).