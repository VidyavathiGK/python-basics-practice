import re

class SlugGenerator:
    """A utility for generating clean URL slugs from raw text."""
    
    @staticmethod
    def generate(text: str) -> str:
        """Converts raw text into a URL-friendly slug."""
        if not text:
            return ""
        
        # Convert to lowercase
        slug = text.lower()
        
        # Remove special characters and punctuation, replace whitespace with hyphens
        slug = re.sub(r'[^\w\s-]', '', slug)
        slug = re.sub(r'[\s_-]+', '-', slug).strip('-')
        
        return slug


# --- Example Usage ---
if __name__ == "__main__":
    title = "🚀 Building Full-Stack Django Applications in 2026! (A Beginner's Guide)"
    slug = SlugGenerator.generate(title)
    print(f"Original: {title}")
    print(f"Slug:     {slug}")
