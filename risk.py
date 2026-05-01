def is_high_risk(issue):
    keywords = ["fraud", "hacked", "unauthorized", "money deducted"]

    return any(k in issue.lower() for k in keywords)