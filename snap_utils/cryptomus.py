import os
import json
import hashlib
import base64
import random
from dotenv import load_dotenv
from aiohttp import ClientSession

load_dotenv()
CRYPTOMUS_TOKEN = os.getenv('CRYPTOMUS_TOKEN')
CRYPTOMUS_MERCHANT_ID = os.getenv('CRYPTOMUS_MERCHANT_ID')

def generate_headers(data: str):
    sign = hashlib.md5(
        base64.b64encode(data.encode("ascii")) + CRYPTOMUS_TOKEN.encode("ascii")
    ).hexdigest()

    return {
        "merchant": CRYPTOMUS_MERCHANT_ID,
        "sign": sign,
        "content-type": "application/json"
    }

async def create_invoice(user_id: int, amount: int):
    async with ClientSession() as session:
        json_dumps = json.dumps({
            "amount": str(amount),
            "order_id": f"DONATE-FROM-{user_id}-{random.randint(0, 20000)}-{amount}",
            "currency": "USD",
            "lifetime": 900,
            "subtract": 100
        })

        response = await session.post(
            "https://api.cryptomus.com/v1/payment",
            data=json_dumps,
            headers=generate_headers(json_dumps)
        )
        invoice_data = await response.json()
        invoice_data['user_id'] = user_id
        invoice_data['amount'] = amount
        return invoice_data

async def get_invoice(uuid: str):
    async with ClientSession() as session:
        json_dumps = json.dumps({'uuid': uuid})
        response = await session.post(
            'https://api.cryptomus.com/v1/payment/info',
            data=json_dumps,
            headers=generate_headers(json_dumps)
        )
    return await response.json()