import ipaddress
import requests


def validate_ip(ip: str) -> bool:
    if not ip or not isinstance(ip, str):
        return False
    try:
        ipaddress.ip_address(ip.strip())
        return True
    except ValueError:
        return False


def get_location(ip: str):
    try:
        ipaddress.ip_address(ip.strip())
    except ValueError:
        raise ValueError(f"Invalid IP address: {ip}")

    url: str = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return {
        "country": data["countryName"],
        "region": data["regionName"],
        "city": data["cityName"],
        "code": data["countryCode"],
        "capital": data["capital"],
        "zip": data["zipCode"],
    }
