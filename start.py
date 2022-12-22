import os
import collections
import csv
import string
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

def common_repeated_words(folder_path, csv_file):
    # Initialize an empty list to store the words
    words = []

    # Define a list of stop words to exclude
    stop_words = string.punctuation + string.whitespace + "on in a with of her him them one his she while and no for"

    # Iterate over the files in the folder
    for file in os.listdir(folder_path):
        # Open the file and read the contents
        with open(os.path.join(folder_path, file), 'r') as f:
            contents = f.read()
        # Split the contents into words and add them to the list, excluding stop words
        words += [word for word in contents.split() if word not in stop_words]

    # Use the collections.Counter object to count the occurrences of each word
    word_counts = collections.Counter(words)

    # Sort the word counts in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Open the CSV file for writing
    with open(csv_file, 'w', newline='') as f:
        # Create a CSV writer object
        writer = csv.writer(f)
        # Write the header row
        writer.writerow(['Word', 'Count'])
        # Write the data rows
        for word, count in sorted_word_counts:
            if count > 1:
                writer.writerow([word, count])

folder_path = "files"
csv_file = f'result_{timestamp}.csv'
common_repeated_words(folder_path, csv_file)
print("completed: Saved to " + csv_file)
