from classifier import classify_request, detect_intents
from retriever import retrieve_docs
from risk import is_high_risk


def process_issue(issue, docs):
    request_type = classify_request(issue)
    intents = detect_intents(issue)

    # Retrieve doc + similarity score
    doc, score = retrieve_docs(issue, docs)

    confidence = float(score)

    # Decide product area
    product_area = intents[0]

    # Escalation logic
    if is_high_risk(issue) or confidence < 0.3:
        status = "escalated"
        response = "This issue requires human support. Please contact official support team."
        justification = f"High risk or low confidence ({confidence:.2f})"
    else:
        status = "replied"
        response = doc.strip()
        justification = f"Matched with docs (confidence {confidence:.2f})"

    
    return {
        "status": status,
        "product_area": product_area,
        "response": response,
        "justification": justification,
        "request_type": request_type,
        "confidence": round(confidence, 2),
        "intents": intents
    }