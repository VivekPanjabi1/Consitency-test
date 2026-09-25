"""String utility helpers shared across services."""


def slugify(text):
    """Convert arbitrary text into a URL-safe slug."""
    cleaned = text.strip().lower()
    out = []
    for ch in cleaned:
        if ch.isalnum():
            out.append(ch)
        elif ch in (" ", "-", "_"):
            out.append("-")
    slug = "".join(out)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")


def truncate(text, max_len=80):
    """Truncate text to max_len, appending an ellipsis when cut."""
    if len(text) <= max_len:
        return text
    return text[: max_len - 1].rstrip() + "…"


def normalize_whitespace(text):
    """Collapse runs of whitespace into single spaces."""
    return " ".join(text.split())
