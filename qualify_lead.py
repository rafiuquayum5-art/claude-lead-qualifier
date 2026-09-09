"""
Claude Lead Qualifier
Scores an inbound real estate lead message using Claude's tool/function calling,
and returns a structured recommendation for next action.
"""

import os
import json
from anthropic import Anthropic

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# The "tool" Claude will fill in with structured data instead of free text
lead_scoring_tool = {
    "name": "score_lead",
    "description": "Score a real estate lead based on their message and return structured qualification data.",
    "input_schema": {
        "type": "object",
        "properties": {
            "intent_score": {
                "type": "integer",
                "description": "1-10 score of how ready this lead is to act, 10 being ready now"
            },
            "budget": {
                "type": "string",
                "description": "Budget mentioned or 'not specified'"
            },
            "timeline": {
                "type": "string",
                "description": "Move-in or purchase timeline mentioned"
            },
            "next_action": {
                "type": "string",
                "enum": ["book_showing_now", "send_more_info", "nurture_sequence"],
                "description": "Recommended next action based on the lead's readiness"
            }
        },
        "required": ["intent_score", "budget", "timeline", "next_action"]
    }
}

def qualify_lead(message: str) -> dict:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        tools=[lead_scoring_tool],
        tool_choice={"type": "tool", "name": "score_lead"},
        messages=[
            {"role": "user", "content": f"Score this inbound lead message: {message}"}
        ]
    )

    for block in response.content:
        if block.type == "tool_use":
            return block.input

    return {"error": "No structured result returned"}


if __name__ == "__main__":
    with open("samples.json") as f:
        sample_leads = json.load(f)

    for lead in sample_leads:
        print(f"\nLead message: {lead['message']}")
        result = qualify_lead(lead["message"])
        print("Result:", json.dumps(result, indent=2))
