requests = [
    "Customer needs help with login issue",
    "Client wants to book a consultation",
    "User reports a payment problem",
    "Customer asks about pricing",
    "Client requests technical support"
]

for request in requests:
    if "login" in request.lower() or "technical support" in request.lower():
        category = "Support"
    elif "payment" in request.lower() or "pricing" in request.lower():
        category = "Sales and Billing"
    elif "book" in request.lower() or "consultation" in request.lower():
        category = "Bookings"
    else:
        category = "General"

    print(f"Request: {request}")
    print(f"Category: {category}")
    print("-" * 40)
