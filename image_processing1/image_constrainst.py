def check_image(image):
    if image is None:
        raise ValueError('Image is none.')

    width, height = image.size
    if width == 0 or height == 0:
        raise ValueError('Image is empty.')

    if image.mode not in ['L', 'RGB']:
        raise ValueError('Unsupported format.')


if __name__ == '__main__':
    pass
