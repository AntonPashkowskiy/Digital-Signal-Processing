from PIL import Image
import image_item_processing
import image_filters
import configparser
import glob
import os


def get_settings():
    config_parser = configparser.ConfigParser()
    config_parser.read('./settings.ini')
    return config_parser


def input_file_template(settings):
    directory = settings['input_settings']['directory']
    file_template = settings['input_settings']['file_template']
    return os.path.join(directory, file_template)


def output_path(settings, input_file_path, postfix=''):
    directory = settings['output_settings']['directory']
    file_name = os.path.basename(input_file_path)
    name, extension = os.path.splitext(file_name)
    return os.path.join(directory, name + postfix + extension)


def clear_output_directory(settings):
    path_to_directory = settings['output_settings']['directory']
    file_template = os.path.join(path_to_directory, '*')
    for file in glob.glob(file_template):
        os.remove(file)


def main():
    try:
        settings = get_settings()
        clear_output_directory(settings)
        file_template = input_file_template(settings)

        for input_file_path in glob.glob(file_template):
            image = Image.open(input_file_path)
            image_bi = image_item_processing.brightness_increase(image, settings)
            image_bd = image_item_processing.brightness_decrease(image, settings)
            image_pf = image_filters.previtts_filter(image)
            image_bi.save(output_path(settings, input_file_path, '_bi'))
            image_bd.save(output_path(settings, input_file_path, '_bd'))
            image_pf.save(output_path(settings, input_file_path, '_pf'))

    except Exception as ex:
        raise ex


if __name__ == '__main__':
    main()