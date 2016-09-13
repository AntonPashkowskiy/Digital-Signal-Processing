from matplotlib_wrapper import BarChartPainter


def show_histograms(original_image, decreased_image, increased_image, filtered_image):
    if original_image.mode == 'L':
        __show_histograms_1byte_images(original_image, decreased_image, increased_image, filtered_image)
    elif original_image.mode == 'RGB':
        __show_histograms_3byte_images(original_image, decreased_image, increased_image, filtered_image)


def __show_histograms_3byte_images(original_image, decreased_image, increased_image, filtered_image):
    bar_chart_painter = BarChartPainter("3 byte per pixel", (4, 3))
    red_part = slice(0, 256)
    green_part = slice(256, 512)
    blue_part = slice(512, 768)

    original_image_histogram = original_image.histogram()
    original_image_red_histogram = original_image_histogram[red_part]
    original_image_green_histogram = original_image_histogram[green_part]
    original_image_blue_histogram = original_image_histogram[blue_part]
    bar_chart_painter.append_plot("Original image red", original_image_red_histogram, color="red")
    bar_chart_painter.append_plot("Original image green", original_image_green_histogram, color="green")
    bar_chart_painter.append_plot("Original image blue", original_image_blue_histogram, color="blue")

    decreased_image_histogram = decreased_image.histogram()
    decreased_image_red_histogram = decreased_image_histogram[red_part]
    decreased_image_green_histogram = decreased_image_histogram[green_part]
    decreased_image_blue_histogram = decreased_image_histogram[blue_part]
    bar_chart_painter.append_plot("Decreased brightness red", decreased_image_red_histogram, color="red")
    bar_chart_painter.append_plot("Decreased brightness green", decreased_image_green_histogram, color="green")
    bar_chart_painter.append_plot("Decreased brightness blue", decreased_image_blue_histogram, color="blue")

    increased_image_histogram = increased_image.histogram()
    increased_image_red_histogram = increased_image_histogram[red_part]
    increased_image_green_histogram = increased_image_histogram[green_part]
    increased_image_blue_histogram = increased_image_histogram[blue_part]
    bar_chart_painter.append_plot("Increased brightness red", increased_image_red_histogram, color="red")
    bar_chart_painter.append_plot("Increased brightness green", increased_image_green_histogram, color="green")
    bar_chart_painter.append_plot("Increased brightness blue", increased_image_blue_histogram, color="blue")

    filtered_image_histogram = filtered_image.histogram()
    filtered_image_red_histogram = filtered_image_histogram[red_part]
    filtered_image_green_histogram = filtered_image_histogram[green_part]
    filtered_image_blue_histogram = filtered_image_histogram[blue_part]
    bar_chart_painter.append_plot("Filtered image red", filtered_image_red_histogram, color="red")
    bar_chart_painter.append_plot("Filtered image green", filtered_image_green_histogram, color="green")
    bar_chart_painter.append_plot("Filtered image blue", filtered_image_blue_histogram, color="blue")

    bar_chart_painter.show()


def __show_histograms_1byte_images(original_image, decreased_image, increased_image, filtered_image):
    bar_chart_painter = BarChartPainter("1 byte per pixel", (4, 1))
    bar_chart_painter.append_plot("Original image", original_image.histogram(), color="green")
    bar_chart_painter.append_plot("Decreased brightness", decreased_image.histogram(), color="blue")
    bar_chart_painter.append_plot("Increased brightness", increased_image.histogram(), color="blue")
    bar_chart_painter.append_plot("Filtered image", filtered_image.histogram(), color="blue")
    bar_chart_painter.show()


if __name__ == '__main__':
    pass
