import re

def parse_markdown_with_frontmatter(filepath: str) -> tuple:
    """Parses YAML-style frontmatter from a Markdown file and returns metadata and body content."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        return {}, ""

    # Match YAML frontmatter enclosed in ---
    pattern = re.compile(r"^---\s*(.*?)\s*---\s*(.*)", re.DOTALL)
    match = pattern.match(content)

    if not match:
        return {}, content

    frontmatter_raw, body = match.groups()
    metadata = {}
    
    for line in frontmatter_raw.splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            metadata[key.strip()] = val.strip().strip('"\'')

    return metadata, body.strip()

if __name__ == "__main__":
    sample_content = """---
title: "Getting Started with Python"
author: "Vidyavathi GK"
date: "2026-06-01"
---
# Welcome
This is the body content of the document.
"""
    with open("sample_post.md", "w", encoding="utf-8") as f:
        f.write(sample_content)

    meta, text = parse_markdown_with_frontmatter("sample_post.md")
    print("Extracted Metadata:", meta)
    print("Body Length:", len(text), "characters")
