from flask import Flask
from flask import request
from twilio.rest import Client
import os
from marketstack import get_stock_price

app = Flask(__name__)

acc_id = os.environ.get('account')
auth_token = os.environ.get('token')
client = Client(acc_id, auth_token)
TWILIO_NUMBER = 'whatsapp:+14155238886'

def process_msg(msg):
    response = ""
    if "hi" in msg.lower():
        response = "Hello master, I am your stock market bot. I support 72 global exchanges. and 1,25,000+ stock tickers.\n\nHope I may help you.\n\n"
        response += "Please type \"sym:<stock_symbol>\" to know the price of the stock."
    elif "sym:" in msg.lower():
        data = msg.split(":")
        stock_symbol = data[1]
        stock_data = get_stock_price(stock_symbol)
        response = "=> Stock data of " + stock_symbol + " is:\n\n" + str(stock_data) + "\n\n (Note: Stock values are in USD.)"
    else:
        response = "Please type \"Hi\" to get started."
    return response

def send_msg(msg, recipient):
    client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=recipient
    )

@app.route("/", methods=["POST"])
def webhook():
    f=request.form
    msg = f['Body']
    sender = f['From']
    response = process_msg(msg)
    send_msg(response, sender)
    return"OK", 200


