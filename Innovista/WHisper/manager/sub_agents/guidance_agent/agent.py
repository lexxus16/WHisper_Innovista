from google.adk.agents import Agent

guidance_agent = Agent(
    name="guidance_agent",
    model="gemini-1.5-flash-001",
    description="Matches a case to the right service.",
    instruction="""
    You are a Guidance Agent. Your task is to find the correct frontline service based on the case details provided by the triage agent.
    You will be given a user's problem and an urgency level.
    Analyze this information and identify the single best service from a provided list of services in the context.
    For example, if the issue is a "suspected heart attack," you must recommend an "Emergency Ward" at a hospital. If it's a "fallen tree," recommend the "City Council."
    Your output should be ONLY the name and details of the recommended service.
    """
)