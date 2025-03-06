import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Telegram Bot API Token
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

# Google Sheets API Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Stock Screener").sheet1

# Function to send message to Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

# Fetch Stock Data from Google Sheets
def check_stocks():
    tickers = sheet.col_values(1)[1:]
    signals = sheet.col_values(6)[1:]

    for ticker, signal in zip(tickers, signals):
        if signal.lower() == "buy":
            message = f"{ticker}: BUY Signal Alert! 🚨"
            send_telegram_message(message)

if __name__ == "__main__":
    check_stocks()
