#!/usr/bin/env python3
"""Runner de Gemini 3.5 Flash (thinking high). Uso: _gemini_run.py <prompt_file> <output_file>"""
import sys, os
from google import genai
from google.genai import types

prompt_file, output_file = sys.argv[1], sys.argv[2]
with open(prompt_file, "r") as f:
    prompt_text = f.read()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
try:
    _tc = types.ThinkingConfig(thinking_level="high")
except Exception:
    _tc = types.ThinkingConfig(thinking_budget=-1)

resp = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt_text,
    config=types.GenerateContentConfig(thinking_config=_tc),
)
with open(output_file, "w") as f:
    f.write(resp.text)
print(f"OK gemini -> {output_file} ({len(resp.text)} chars)")
