import os, requests

INSTANCE = os.getenv("GREEN_API_INSTANCE_ID")
TOKEN    = os.getenv("GREEN_API_TOKEN")
BASE_URL = f"https://api.green-api.com/waInstance{INSTANCE}/sendMessage/{TOKEN}"


def normalize_phone(number):
    return number.replace("+", "").replace(" ", "").strip() + "@c.us"

def send_whatsapp(chat_id, message):
    resp = requests.post(
        BASE_URL,
        json={"chatId": chat_id, "message": message},
        timeout=10
    )

    resp.raise_for_status()