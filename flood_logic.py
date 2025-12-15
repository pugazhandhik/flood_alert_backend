def check_flood_risk(water_level, rainfall):
    if water_level > 5 or rainfall > 100:
        return "HIGH"
    elif water_level > 3 or rainfall > 50:
        return "MEDIUM"
    else:
        return "LOW"
