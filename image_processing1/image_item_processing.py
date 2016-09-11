from PIL import Image
from image_constrainst import check_image


max_brightness = 255


def brightness_increase(image, settings):
    check_image(image)
    max_input_brightness = int(settings['brightness_increase_settings']['input_max'])
    min_output_brightness = max_brightness - max_input_brightness
    if image.mode == 'L':
        return __process_image_1byte(image, __increase_brightness, max_input_brightness, min_output_brightness)
    elif image.mode == 'RGB':
        return __process_image_3byte(image, __increase_brightness, max_input_brightness, min_output_brightness)


def __increase_brightness(value, max_input_brightness, min_output_brightness):
    if 0 <= value <= max_input_brightness:
        return min_output_brightness + value
    elif max_input_brightness < value <= max_brightness:
        return max_brightness
    else:
        return max_brightness


def brightness_decrease(image, settings):
    check_image(image)
    max_output_brightness = int(settings['brightness_decrease_settings']['output_max'])
    min_input_brightness = max_brightness - max_output_brightness
    if image.mode == 'L':
        return __process_image_1byte(image, __decrease_brightness, min_input_brightness, max_output_brightness)
    elif image.mode == 'RGB':
        return __process_image_3byte(image, __decrease_brightness, min_input_brightness, max_output_brightness)


def __decrease_brightness(value, min_input_brightness, max_output_brightness):
    if 0 <= value <= min_input_brightness:
        return 0
    elif min_input_brightness < value < max_brightness:
        return value - min_input_brightness
    elif value == max_brightness:
        return max_output_brightness


def __process_image_1byte(image, processing_function, *processing_args):
    output_image = Image.new(image.mode, image.size)
    width, height = image.size

    for y in range(0, height):
        for x in range(0, width):
            pixel = image.getpixel((x, y))
            output_pixel = processing_function(pixel, *processing_args)
            output_image.putpixel((x, y), output_pixel)
    return output_image


def __process_image_3byte(image, processing_function, *processing_args):
    output_image = Image.new(image.mode, image.size)
    width, height = image.size

    for y in range(0, height):
        for x in range(0, width):
            red, green, blue = image.getpixel((x, y))
            output_red = processing_function(red, *processing_args)
            output_green = processing_function(green, *processing_args)
            output_blue = processing_function(blue, *processing_args)
            output_image.putpixel((x, y), (output_red, output_green, output_blue))
    return output_image


if __name__ == '__main__':
    pass
