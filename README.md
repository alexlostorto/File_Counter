<h1 align="center">File Counter</h1>

The program goes through each file in a chosen directory and counts all the lines, words and characters.

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

1) The coordinate for each four point moving average is printed.

``` python
    for i in range(len(x2)):
        print(f"{x2[i]}, {y2[i]}")
```

## Screenshots
<p align="center"><img width="80%" src="https://github.com/alexlostorto/Statistics/raw/main/git_images/four_point_moving_averages.png" alt="four point moving averages displayed on a graph using matplotlib" /></p>

## Credits 

Everything is coded by Alex lo Storto

Licensed under the MIT License.
