import requests

# criando conta na ethereal.email
payload = {
    "requestor": "naruhiko_testing_email",
    "version": "1.0"
}

response = requests.post("https://api.nodemailer.com/user", json=payload)

if response.status_code == 200:
    account = response.json()
    print(account)

else:
    raise Exception("Failed to create account")