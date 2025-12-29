import pandas as pd
from .risk_model import classify_risk

def apply_scenario(df, demand_shock = 0.0, court_loss = 0):
    stressed = df.copy() # make copy of df 

    stressed["stressed_demand"] = ( # stress demand 
        stressed["booked_courts"] * (1+demand_shock) # percentage increase 
    ).round().astype(int)

    stressed["stressed_capacity"] = ( # stress capacity
        stressed["total_courts"] - court_loss
    ).clip(lower = 1) # lowest value is 1 (lower than 1 becomes 1)

    stressed["stressed_utilisation"] = ( # new utilisation
        stressed["stressed_demand"] / stressed["stressed_capacity"]
    ).round(1)

    stressed["stressed_rs"] = ( # new risk score
        0.5*stressed["stressed_utilisation"] + 
        0.3*stressed["peak_hour_flag"] + 
        0.2*stressed["weekend_flag"]
    ).round(2)

    stressed["stressed_rl"] = ( # new risk level
        stressed["stressed_rs"].apply(classify_risk)
    )

    return stressed