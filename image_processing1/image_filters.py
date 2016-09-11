from image_constrainst import check_image
from scipy import signal
from PIL import Image
import numpy

previtts_kernel1 = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]
previtts_kernel2 = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]
brightness_min = 0
brightness_max = 255


def previtts_filter(image):
    check_image(image)
    if image.mode == 'L':
        return __filter_image(image, __previtts_filter_1byte)
    elif image.mode == 'RGB':
        return __filter_image(image, __previtts_filter_3byte)


def __previtts_filter_1byte(image_matrix):
    first_response = signal.convolve2d(image_matrix, previtts_kernel1, 'same')
    second_response = signal.convolve2d(image_matrix, previtts_kernel2, 'same')
    return union_responses(first_response, second_response)


def __previtts_filter_3byte(image_matrix):
    red_matrix, green_matrix, blue_matrix = __split_3byte_image_matrix(image_matrix)
    red_matrix_response = __previtts_filter_1byte(red_matrix)
    green_matrix_response = __previtts_filter_1byte(green_matrix)
    blue_matrix_response = __previtts_filter_1byte(blue_matrix)
    return __concat_3byte_image_matrix(red_matrix_response, green_matrix_response, blue_matrix_response)


def __split_3byte_image_matrix(image_matrix):
    red_matrix = []
    green_matrix = []
    blue_matrix = []
    for y in range(0, len(image_matrix)):
        red_line = []
        green_line = []
        blue_line = []
        for x in range(0, len(image_matrix[y])):
            red, green, blue = image_matrix[y][x]
            red_line.append(red)
            green_line.append(green)
            blue_line.append(blue)
        red_matrix.append(red_line)
        green_matrix.append(green_line)
        blue_matrix.append(blue_line)
    return red_matrix, green_matrix, blue_matrix


def __concat_3byte_image_matrix(red_matrix, green_matrix, blue_matrix):
    # zipping of 3 matrix in 1 matrix with tuple (r, g, b)
    return [[(red_line[index], green_line[index], blue_line[index]) for index in range(len(red_line))]
            for red_line, green_line, blue_line in zip(red_matrix, green_matrix, blue_matrix)]


def __filter_image(image, filter_function):
    output_image = Image.new(image.mode, image.size)
    image_matrix = __get_image_as_matrix(image)
    filtered_image_matrix = filter_function(image_matrix)
    __populate_image_by_matrix(output_image, filtered_image_matrix)

    return output_image


def __get_image_as_matrix(image):
    width, height = image.size
    result = []
    for y in range(0, height):
        line = []
        for x in range(0, width):
            line.append(image.getpixel((x, y)))
        result.append(line)
    return result


def __populate_image_by_matrix(image, matrix):
    width, height = image.size
    for y in range(0, height):
        for x in range(0, width):
            pixel_value = __check_pixel_value(matrix[y][x], image.mode)
            image.putpixel((x, y), pixel_value)


def union_responses(first_response, second_response):
    first_response_2 = numpy.power(first_response, 2)
    second_response_2 = numpy.power(second_response, 2)
    response_sum = numpy.add(first_response_2, second_response_2)
    return numpy.sqrt(response_sum)


def __check_pixel_value(value, mode):
    if mode == 'L':
        return __check(value)
    elif mode == 'RGB':
        red, green, blue = value
        return __check(red), __check(green), __check(blue)


def __check(brightness_value):
    if brightness_value < brightness_min:
        return brightness_min
    elif brightness_value > brightness_max:
        return brightness_max
    return int(brightness_value)


if __name__ == '__main__':
    pass
