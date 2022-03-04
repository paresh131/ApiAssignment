import requests

url = "https://api.thedogapi.com/v1/votes"

payload = ""
headers = {
  'x-api-key': 'bb8f4110-ed96-4552-a939-25c2f8285837'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
#