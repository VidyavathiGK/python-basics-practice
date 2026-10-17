import re

def convert_markdown_to_html(markdown_text):
    # Convert headers (# Header)
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', markdown_text, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    
    # Convert bold (**text**)
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    
    # Convert italics (*text*)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    return html

# Example usage:
if __name__ == "__main__":
    sample_md = "# Hello World\nThis is **bold** text and this is *italic* text."
    print("--- HTML Output ---")
    print(convert_markdown_to_html(sample_md))
