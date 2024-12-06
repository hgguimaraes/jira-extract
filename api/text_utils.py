import unicodedata

def extract_text(comment_body):
    if isinstance(comment_body, dict) and "content" in comment_body:
        return " ".join(
            item.get("text", "") for content in comment_body.get("content", [])
            for item in content.get("content", []) if "text" in item
        )
    return comment_body if isinstance(comment_body, str) else ""

def normalize_text(text):
    if text:
        text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
        return text
    return ""