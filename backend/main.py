from typing import List
from pathlib import Path

from PIL import Image
from transformers import pipeline

# Lazy global so the first call downloads/loads the model, subsequent calls reuse it
_captioner = None


def _get_captioner():
    global _captioner
    if _captioner is None:
        # BLIP captioning model: small and widely used
        _captioner = pipeline(
            "image-to-text",
            model="Salesforce/blip-image-captioning-base",
        )
    return _captioner


def _keywords_from_caption(caption: str) -> List[str]:
    """Very naive keyword split; good enough for MVP. You can later swap for keyphrase extraction."""
    cleaned = caption.replace(".", " ").replace(",", " ")
    parts = [p.strip().lower() for p in cleaned.split() if p.strip()]
    # keep unique order-preserving words longer than 2 chars
    seen = set()
    out = []
    for w in parts:
        if len(w) <= 2:
            continue
        if w in seen:
            continue
        seen.add(w)
        out.append(w)
    # cap to 10 tags for MVP
    return out[:10]


def generate_tags(file_path: str, media_type: str) -> List[str]:
    """
    Generate simple tags from an image (photo) using BLIP captioning.
    For videos: returns a placeholder for now; you can add keyframe extraction later.
    """
    path = Path(file_path)
    if media_type == "photo":
        if not path.exists():
            return ["photo"]
        img = Image.open(path).convert("RGB")
        captioner = _get_captioner()
        result = captioner(img)
        # pipeline returns a list of dicts like { 'generated_text': 'a caption' }
        caption = result[0]["generated_text"] if result else ""
        tags = _keywords_from_caption(caption)
        # Ensure at least one generic tag
        return tags or ["photo"]
    elif media_type == "video":
        # Placeholder until keyframe extraction is added
        return ["video"]
    return []
