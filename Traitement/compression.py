from PIL import Image


def compression_quality_photo(src, quality, format=None):
    image = Image.open(src)

    if format is None:
        format = image.format

    try:
        image.save(src.path, format=format, quality=quality)
    except:
        image.save(src, format=format, quality=quality)

    image.close()


def compression_size_photo(src, size):
    image = Image.open(src)

    max_var = max([image.size[0] / size, image.size[1] / size])
    if max_var>1:
        new_size = (int(image.size[0] / max_var), int(image.size[1] / max_var))

        new_image = image.resize(new_size, Image.ANTIALIAS)

        try:
            new_image.save(src.path)
        except:
            new_image.save(src)

    image.close()
