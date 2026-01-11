#!/usr/bin/env python3
from __future__ import annotations

from codex_sdk import Codex

codex = Codex()
thread = codex.start_thread()

schema = {
    "type": "object",
    "properties": {
        "summary": {"type": "string"},
        "status": {"type": "string", "enum": ["ok", "action_required"]},
    },
    "required": ["summary", "status"],
    "additionalProperties": False,
}

turn = thread.run("Summarize repository status", output_schema=schema)
print(turn.final_response)
