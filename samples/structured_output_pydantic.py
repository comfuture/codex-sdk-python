#!/usr/bin/env python3
from __future__ import annotations

from pydantic import BaseModel

from codex_sdk import Codex


class SummarySchema(BaseModel):
    summary: str
    status: str


codex = Codex()
thread = codex.start_thread()

turn = thread.run("Summarize repository status", output_schema=SummarySchema)
print(turn.final_response)
