import msal

client_id = '77c0e3e0-c86c-493c-89b6-36db2c05f9d7'
client_secret = '.X78Q~jqH1TxmOECyYrcNIVRpY2BuCwk5vrxOaej'
tenant_id = '0432a8f6-b5b3-4e3f-89ae-d7448f92f41d'

authority = f"https://login.microsoftonline.com/{tenant_id}"
scope = ["https://graph.microsoft.com/.default"]

app = msal.ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)
result = app.acquire_token_for_client(scopes=scope)

print(result)
#exit()

access_token = result['access_token']

import requests

headers = {
    "Authorization": f"Bearer {access_token}"
}

graph_url = "https://graph.microsoft.com/v1.0/users"

res = requests.get(graph_url, headers=headers)
for u in res.json().get("value", []):
    print(u["id"], u["userPrincipalName"])




user_email = "super#@thuchanhhnvgmail.onmicrosoft.com"  # User mà bạn muốn lấy file
user_id = "e2038aab-9d9d-4dc8-b4b7-5cc0ab229239"
file_path = "/download_data/campaigns.xlsx"  # Đường dẫn đến file
graph_url = f"https://graph.microsoft.com/v1.0/users/{user_id}/drive/root:{file_path}:/content"

response = requests.get(graph_url, headers=headers)

if response.status_code == 200:
    with open("downloaded_file.xlsx", "wb") as f:
        f.write(response.content)
    print("✅ File downloaded successfully")
else:
    print(f"❌ Failed: {response.status_code} {response.text}")

