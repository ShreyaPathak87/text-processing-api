def summarize_text(text: str):

    if not text:
        return ""

    # simple real transformation (not echo)
    words = text.split()

    if len(words) <= 10:
        return text

    return " ".join(words[:10]) + "..."