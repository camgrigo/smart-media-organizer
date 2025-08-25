def generate_tags(file_path: str, media_type: str) -> list[str]:
    """
    Placeholder for AI tagging.
    Photos -> image model
    Videos -> key frame extraction + image model
    """
    if media_type == "photo":
        return ["example-photo", "tag"]
    elif media_type == "video":
        return ["example-video", "tag"]
    return []
