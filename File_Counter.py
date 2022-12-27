import os

# Absolute path to the directory you want to search
ROOT = r"C:\Users\[Users]\[pythonFiles]"
FILE_LIST = []
SUFFIX = '.py'
USE_SUFFIX = True
COUNT_LINES = True
COUNT_WORDS = False
COUNT_CHARACTERS = False
EXCLUDE_SPACES = True  # As a character
TOTAL_LINES = 0
TOTAL_WORDS = 0
TOTAL_CHARACTERS = 0


def print_data(path):
    global TOTAL_LINES
    global TOTAL_WORDS
    global TOTAL_CHARACTERS

    if COUNT_LINES:
        lines = count_lines(path)
        TOTAL_LINES += lines
        print(f"Lines: {lines}")
    if COUNT_WORDS:
        words = count_words(path)
        TOTAL_WORDS += words
        print(f"Words: {words}")
    if COUNT_CHARACTERS:
        chars = count_characters(path)
        TOTAL_CHARACTERS += chars
        print(f"Characters: {chars}")


def count_lines(file_path):
    try:
        with open(file_path, 'r') as f:
            line_count = 0
            for line in f:
                if line != "\n":
                    line_count += 1
    except:
        print("Couldn't count lines")
        return 0

    return line_count


def count_words(file_path):
    try:
        with open(file_path, 'r') as f:
            data = f.read()
            words = data.split()

        word_count = len(words)
    except:
        print("Couldn't count words")
        return 0

    return word_count


def count_characters(file_path):
    try:
        with open(file_path, 'r') as f:
            if EXCLUDE_SPACES:
                data = f.read().replace(" ", "")
            else:
                data = f.read()

        char_count = len(data)
    except:
        print("Couldn't count characters")
        return 0

    return char_count


def main():
    assert os.path.isdir(ROOT)
    for root, dirs, files in os.walk(ROOT):
        for file in files:
            # append the file name to the list if it ends with '.py'
            path = os.path.join(root, file)
            if file.endswith(SUFFIX) and USE_SUFFIX:
                FILE_LIST.append(path)
                print(path)
                print_data(path)
            elif not USE_SUFFIX:
                FILE_LIST.append(path)
                print(path)
                print_data(path)

    print(f"\nFiles checked: {len(FILE_LIST):,}")
    if COUNT_LINES:
        print(f"Total lines: {TOTAL_LINES:,}")
    if COUNT_WORDS:
        print(f"Total words: {TOTAL_WORDS:,}")
    if COUNT_CHARACTERS:
        print(f"Total characters: {TOTAL_CHARACTERS:,}")

    # print all the file names
    # for name in FILE_LIST:
    #     print(name)


if __name__ == '__main__':
    main()
