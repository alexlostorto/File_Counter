<h1 align="center">File Counter</h1>

The program goes through each file in a chosen directory and counts all the lines, words and characters.

``` python
# Example in console
Files searched: 70
Total lines: 15,076
Total words: 65,678
Total characters: 2,067,234
```

## How it Works 

Below is a list of all the variables you can choose to alter:

``` python
ROOT = r"C:\Users\[Users]\[pythonFiles]"  # Absolute path to the directory you want to search
FILE_LIST = []  # List of all the files searched
SUFFIX = '.py'  # Only search files with the chosen suffix
USE_SUFFIX = True  # Search all files or only files ending in this suffix
COUNT_LINES = True  # Choose to count lines
COUNT_WORDS = False  # Choose to count words
COUNT_CHARACTERS = False  # Choose to count characters
EXCLUDE_SPACES = True  # Choose to count or exclude spaces
```

1) Check if the ROOT path is a directory

``` python
assert os.path.isdir(ROOT)
```

2) Using os.walk() we can traverse recursively through all the subdirectories of the ROOT directrory. By using a for loop to loop over all the files in each directory, we can calculate the amount of lines, words and characters in each file.

``` python
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
```

## Counting Functions

#### Line Counter

Loops over each line in a file and if it isn't a blank line ('\n'), it will add 1 to the line_count.

``` python
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
```

#### Word Counter

Reads all the data from the file and splits the text into words using .split(). The word count is calculated by finding the length of the words list, using the len() function.

``` python
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
```

#### Character Counter

Reads the file and calculates the character count by finding the length of the data, using the len() function.

``` python
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
```

## Credits 

Everything is coded by Alex lo Storto

Licensed under the MIT License.
