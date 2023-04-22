# Importing library
import requests 

# Take Data from user 
Amount = input('Enter Amount that is to be converted: ')
print('ENTER CURRENCIES-> ')
From = input('Initial currency: ').upper()
To = input('Final currency: ').upper()

url = f"https://api.apilayer.com/currency_data/convert?to={To}&from={From}&amount={Amount}"
payload = {}
headers = {
  "apikey": ***********************
}
response = requests.request("GET", url, headers=headers, data = payload)
status_code = response.status_code
result = response.text
print(result)
