# Claude Lead Qualifier

An AI agent that reads an inbound lead message and instantly scores it — intent, budget, timeline, and recommended next action — using Claude's tool/function calling instead of manual review.

## The problem this solves

Slow lead follow-up costs sales. Sales and support teams often let inbound messages sit for hours before someone manually decides whether a lead is worth chasing. This script shows how Claude can make that call in seconds, structured and consistent every time.

## How it works

1. A lead message comes in (e.g. from a website form, chat, or CRM webhook).
2. The script sends it to Claude along with a defined `score_lead` tool.
3. Claude returns structured JSON: an intent score (1-10), budget, timeline, and a recommended next action (`book_showing_now`, `send_more_info`, or `nurture_sequence`).
4. That structured output can be piped directly into a CRM, calendar booking system, or automation platform like Make or n8n.

## Example output
