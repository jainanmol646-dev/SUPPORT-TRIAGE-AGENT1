def classify_request(issue):
    issue = issue.lower()

    if "error" in issue or "bug" in issue:
        return "bug"
    elif "feature" in issue:
        return "feature_request"
    elif "how" in issue or "help" in issue:
        return "product_issue"
    else:
        return "invalid"


def detect_intents(issue):
    issue = issue.lower()
    intents = []

    if "payment" in issue or "money" in issue:
        intents.append("billing")
    if "login" in issue or "password" in issue:
        intents.append("authentication")
    if "assessment" in issue or "test" in issue:
        intents.append("assessment")

    return intents if intents else ["general"]