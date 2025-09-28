from google.adk.agents import Agent
from ...tools.tools import book_api_appointment, draft_email_to_service
from google.adk.tools.agent_tool import AgentTool

booking_agent = Agent(
    name="booking_agent",
    model="gemini-1.5-flash-001",
    description="Books appointments and drafts communications.",
    instruction="""
    You are a Booking Agent. Your job is to take the service details provided by the guidance agent and secure a booking or initiate contact.
    Use the tools available to you to perform the required action.
    - If the service has a booking API, use the `book_api_appointment` tool.
    - If the service requires an email, use the `draft_email_to_service` tool.
    Your output must be a simple confirmation object, including the status and any confirmation ID. Example: {"status": "Booked", "confirmation_id": "XYZ123", "service_name": "City General Hospital"}
    """,
    
tools=[
    AgentTool(book_api_appointment),
    AgentTool(draft_email_to_service),
]
)