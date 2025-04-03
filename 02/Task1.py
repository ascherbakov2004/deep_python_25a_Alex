import json
from typing import Callable

def process_json(
    json_str: str,
    required_keys: list[str] | None = None,
    tokens: list[str] | None = None,
    callback: Callable[[str, str], None] | None = None,
) -> None:
    if required_keys is None or tokens is None or callback is None:
        return

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        return

    lowered_tokens = [token.lower() for token in tokens]

    for key, value in data.items():
        if key in required_keys:
            words = value.split()
            for word in words:
                if word.lower() in lowered_tokens:
                    callback(key, word)
