import argparse
import os

def read_locale_file(file_name):
    """
    Reads the locale file and returns a list of available locales.
    """
    locales = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                fields = line.strip().split(',')
                if len(fields) == 3 and fields[0] == 'locale':
                    locales.append(fields[2])
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        exit(1)
    except IOError:
        print(f"Error: Unable to read file '{file_name}'.")
        exit(1)
    return locales

def print_available_locales(file_name):
    """
    Prints the filenames of all available locales.
    """
    locales = read_locale_file(file_name)
    if locales:
        print("Available locales:")
        for locale in locales:
            print(locale)
    else:
        print("No locales available")

def main():
    parser = argparse.ArgumentParser(description='Parse locale file and list available locales.')
    parser.add_argument('file', metavar='FILE', type=str, help='the locale file to parse')
    args = parser.parse_args()

    file_name = args.file

    if not os.path.isfile(file_name) or not os.access(file_name, os.R_OK):
        print(f"Error: File '{file_name}' does not exist or is not readable.")
        exit(1)

    print_available_locales(file_name)

if __name__ == "__main__":
    main()
