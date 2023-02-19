import requests
Start = input('Enter start data(YYYY-MM-DD): ')
END = input('Enter end data(YYYY-MM-DD): ')
url = f"https://api.apilayer.com/currency_data/change?start_date={Start}&end_date={END}"

payload = {}
headers= {
  "apikey": ***********************
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)
