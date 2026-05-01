import pandas as pd
from agent import process_issue
from retriever import load_docs

df = pd.read_csv("data/support_issue.csv")
docs = load_docs()

for i, row in df.iterrows():
    result = process_issue(row["issue"], docs)

    print("\n====== SUPPORT RESULT ======")
    print(f"Issue: {row['issue']}")
    print(f"Status: {result['status']}")
    print(f"Product Area: {result['product_area']}")
    print(f"Response: {result['response']}")
    print(f"Reason: {result['justification']}")
    print(f"Type: {result['request_type']}")
    print(f"Confidence: {result['confidence']}")
    print(f"Intents: {result['intents']}")
    print("============================")