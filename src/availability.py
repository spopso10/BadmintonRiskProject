def search_available(df, date, hour):
    filtered = df[
        (df["date"] == date) & # match by date and hour
        (df["hour"] == hour)
    ].copy()

    filtered["available_courts"] = ( #create new column
        filtered["total_courts"] - filtered["booked_courts"]
    )

    feasible = filtered[filtered["available_courts"] > 0] 
    # available only if available courts > 0 

    result = (
        feasible
        .sort_values("risk_score") # sort by risk_score 
        [["venue", "available_courts", "risk_score", "risk_level"]] # show only 3 columns 
    )

    return result