from period.core.draw import draw


def alert(text='Hello, world!', animation_offset=3):
    tokens = text.split()

    text_size = draw.textsize(text=text)
    xy = (round((draw.device.size[0] - text_size[0]) / 2),
          round((draw.device.size[1] - text_size[1]) / 2))

    for token in tokens:
        for height in range(animation_offset):
            display_text = ' '.join(tokens[:tokens.index(token)])
            offset = draw.textsize(text=f'{display_text} ')[0]

            draw.text(xy=xy, text=display_text, fill=True)
            draw.text(xy=(xy[0] + offset, xy[1] + (animation_offset - height) - 1), text=token, fill=True)
            draw.clear()
