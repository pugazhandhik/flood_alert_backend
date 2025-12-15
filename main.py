from fastapi import FastAPI
from models import FloodData
from flood_logic import check_flood_risk
from sms_service import send_sms

app = FastAPI()

PHONE_NUMBERS = ["+91xxxxxxxxxx"]

@app.post("/flood/check")
def flood_check(data: FloodData):

    risk = check_flood_risk(data.water_level, data.rainfall)

    if risk == "HIGH":
        alert = "⚠️ FLOOD ALERT! Move to safe location from government."
        send_sms(PHONE_NUMBERS, alert)

    return {
        "risk_level": risk,
        "water_level": data.water_level,
        "rainfall": data.rainfall
    }
