def classify_risk(score):
    if score < 0.4: # if lower than 0.4
        return "Low"
    elif score <= 0.7: # if 0.4 <= score <= 0.7
        return "Medium"
    else: # higher than 0.7
        return "High"