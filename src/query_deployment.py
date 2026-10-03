"""Query an IBM Cloud ML deployment without storing credentials in source."""
import json
import os
from pathlib import Path
import requests

API_KEY = os.getenv("IBM_CLOUD_API_KEY")
DEPLOYMENT_URL = os.getenv("IBM_CLOUD_DEPLOYMENT_URL")
TOKEN_URL = "https://iam.cloud.ibm.com/identity/token"

if not API_KEY or not DEPLOYMENT_URL:
    raise SystemExit("Set IBM_CLOUD_API_KEY and IBM_CLOUD_DEPLOYMENT_URL in the environment.")

token_response = requests.post(
    TOKEN_URL,
    data={"apikey": API_KEY, "grant_type": "urn:ibm:params:oauth:grant-type:apikey"},
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    timeout=30,
)
token_response.raise_for_status()
access_token = token_response.json()["access_token"]

payload_path = Path("payload.json")
if not payload_path.exists():
    raise SystemExit("Create payload.json using the input schema expected by your deployment.")
payload = json.loads(payload_path.read_text(encoding="utf-8"))
response = requests.post(
    DEPLOYMENT_URL,
    json=payload,
    headers={"Content-Type": "application/json", "Authorization": f"Bearer {access_token}"},
    timeout=60,
)
response.raise_for_status()
print(json.dumps(response.json(), indent=2))

