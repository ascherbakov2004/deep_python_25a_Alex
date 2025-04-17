import json
from typing import Callable, List, Optional

def process_json(
    json_str: str,
    required_keys: Optional[List[str]] = None,
    tokens: Optional[List[str]] = None,
    callback: Optional[Callable[[str, str], None]] = None,
) -> None:
    required_keys = required_keys or []
    tokens = tokens or []
    callback = callback or (lambda key, token: None)

    if not isinstance(json_str, str):
        return

    if not (required_keys and tokens):
        return
    if not (
        isinstance(required_keys, list)
        and all(isinstance(key, str) for key in required_keys)
    ):
        return
    if not (
        isinstance(tokens, list) and all(isinstance(token, str) for token in tokens)
    ):
        return

    try:
        json_doc = json.loads(json_str)
    except json.JSONDecodeError:
        return

    for key in required_keys:
        if key in json_doc and isinstance(json_doc[key], str):
            for word in json_doc[key].split():
                if any(token.lower() == word.lower() for token in tokens):
                    callback(key, word)

