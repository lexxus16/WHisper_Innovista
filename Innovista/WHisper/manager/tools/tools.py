from google.adk.tools import tool
import datetime
import random

@tool
def book_api_appointment(service_name: str, reason: str) -> dict:
    """
    Simulates booking an appointment with a service that has an API.
    Args:
        service_name: The name of the service to book with.
        reason: The reason for the appointment.
    Returns:
        A dictionary containing a mock confirmation.
    """
    print(f"INFO: Mock booking for '{service_name}' due to '{reason}'.")
    confirmation_id = f"BK-{random.randint(1000, 9999)}"
    appointment_time = datetime.datetime.now() + datetime.timedelta(days=1)
    return {
        "status": "Success",
        "confirmation_id": confirmation_id,
        "service_name": service_name,
        "appointment_time": appointment_time.strftime("%Y-%m-%d %H:%M"),
        "notes": "Please bring your ID card and relevant documents."
    }

@tool
def draft_email_to_service(service_email: str, citizen_request: str) -> dict:
    """
    Simulates drafting an email to a service provider.
    Args:
        service_email: The email address of the service.
        citizen_request: The summary of the citizen's request.
    Returns:
        A dictionary confirming the draft was created.
    """
    print(f"INFO: Mock email drafted for '{service_email}' regarding '{citizen_request}'.")
    return {
        "status": "Email Drafted",
        "recipient": service_email,
        "subject": f"New Citizen Request: {citizen_request[:30]}...",
        "notes": "The request has been forwarded to the appropriate department."
    }