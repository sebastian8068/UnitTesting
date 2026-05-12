import unittest
import requests
from src.api_client import get_location, validate_ip
from unittest.mock import MagicMock, patch


class ApiClientTests(unittest.TestCase):

    @patch("src.api_client.requests.get")
    def test_get_location_returns_correct_data(self, mock_get: MagicMock):
        mock_get.return_value = unittest.mock.Mock(
            status_code=200,
            json=lambda: {
                "countryName": "USA",
                "cityName": "FLORIDA",
                "regionName": "MIAMI",
                "countryCode": "US",
                "capital": "Washington",
                "zipCode": "94035",
            },
        )
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "MIAMI")
        self.assertEqual(result.get("city"), "FLORIDA")
        self.assertEqual(result.get("code"), "US")
        self.assertEqual(result.get("capital"), "Washington")
        self.assertEqual(result.get("zip"), "94035")

        mock_get.assert_called_once_with(
            "https://freeipapi.com/api/json/8.8.8.8"
        )

    @patch("src.api_client.requests.get")
    def test_get_location_raises_on_api_error(self, mock_get: MagicMock):
        mock_get.side_effect = requests.exceptions.RequestException(
            "Service Unavailable"
        )

        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

    def test_validate_ip_returns_true_for_valid_ip(self):
        valid_ips = [
            "8.8.8.8",
            "192.168.1.1",
            "10.0.0.1",
            "255.255.255.255",
            "::1",
            "2001:db8::1",
        ]
        for ip in valid_ips:
            with self.subTest(ip=ip):
                self.assertTrue(validate_ip(ip))

    def test_validate_ip_returns_false_for_invalid_ip(self):
        invalid_ips = [
            "invalid",
            "999.999.999.999",
            "abc.def.ghi.jkl",
            "",
            "   ",
            "192.168.1.1/24",
        ]
        for ip in invalid_ips:
            with self.subTest(ip=ip):
                self.assertFalse(validate_ip(ip))

    @patch("src.api_client.requests.get")
    def test_get_location_raises_on_invalid_ip(self, mock_get: MagicMock):
        with self.assertRaises(ValueError):
            get_location("invalid-ip")
