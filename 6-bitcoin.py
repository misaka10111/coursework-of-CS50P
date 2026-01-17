# Bitcoin Price Index
import sys
import requests
import json

def main():
    try:
        coins = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=6f077700b46dfbfee732c95d8aea6f8318369fcb1d766d403cc84d47c05b4fb1")
        response_dict = response.json()
        data_dict = response_dict["data"]
        result = coins * float(data_dict["priceUsd"])
        print(f"${result:,.4f}")
    except requests.RequestException:
        print("Request Error")


main()
