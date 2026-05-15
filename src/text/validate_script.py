def validate_script(script):
    """
    Prevent extremely short stories
    """
    word_count = len(script.split())

    if word_count < 50 :
        raise ValueError(
            f"Script too short"
            f"({word_count} Words)"
            f"Minimum 50 words required"
        )
    print(
        f"Script validation passed"
        f"({word_count}words)"
    )