import re
import datetime
import os

def generate_metadata(text, filename):
    words = re.findall(r'\b\w+\b', text.lower())
    stop_words = {"the", "and", "is", "in", "to", "of", "a", "for", "on", "with", "as", "by", "an", "are"}
    filtered = [w for w in words if w not in stop_words]

    freq = {}
    for w in filtered:
        freq[w] = freq.get(w, 0) + 1
    top_keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]

    metadata = {
        "created_time": str(datetime.datetime.now()),
        "file_type": f"image/{os.path.splitext(filename)[1][1:]}" if filename.endswith(('.jpg', '.png')) else filename.split('.')[-1],
        "filename": filename,
        "keywords": [k for k, _ in top_keywords],
        "language": "en",
        "summary": text[:150].replace('\n', ' ') + "...",
        "title": ' '.join(words[:5]),
        "word_count": len(words)
    }

    return metadata
