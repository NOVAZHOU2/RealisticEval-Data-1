import emoji


def move_emojis_to_end(s):
    # move emojis to end of response, to avoid subtitles getting out of sync
    emojis = ''
    text_without_emojis = ''
    for i in s.strip():
        try:
            if i in emoji.EMOJI_DATA:
                emojis += i
            else:
                text_without_emojis += i
        except:
            text_without_emojis += i
    text_with_emojis_moved_to_end = f'{text_without_emojis} {emojis}'
    # removing an emoji can leave an unwanted space before certain punctuation. let's clean that up.
    replacements = [
        (' ,', ','),
        (' .', '.'),
        (' ?', '?'),
        (' !', '!'),
        (' }', '}'),
        (' )', ')'),
        (' ]', ']'),
        (' ;', ';'),
        (' :', ':'),
        ('  ', ' '),
    ]
    for old, new in replacements:
        text_with_emojis_moved_to_end = text_with_emojis_moved_to_end.replace(old, new)
    return text_with_emojis_moved_to_end.strip()
