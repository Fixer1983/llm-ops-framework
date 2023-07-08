def format_response(resp: dict) -> str:
    return f"Response: {resp.get('text', '')}"
