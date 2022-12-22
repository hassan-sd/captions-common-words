import os
import collections
import csv
import string
from datetime import datetime
import re
import nltk

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
nltk.download('punkt')

def common_repeated_words(folder_path, csv_file, csv_file_phrases):
    # Initialize an empty list to store the words
    words = []

    # Define a list of stop words to exclude
    stop_words = string.punctuation + string.whitespace + "on in a with of her him them one his she while and no for "

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

    # Initialize an empty list to store the phrases
    phrases = []

    # Iterate over the files in the folder
    for file in os.listdir(folder_path):
        # Open the file and read the contents
        with open(os.path.join(folder_path, file), 'r') as f:
            contents = f.read()
            
            min_phrase_length = 2

            # Split the text into sentences
            sentences = nltk.sent_tokenize(contents)

            # Split each sentence into words and add the resulting phrases to the list
            for sentence in sentences:
                words = nltk.word_tokenize(sentence)
                for i in range(len(words) - min_phrase_length + 1):
                    phrase = words[i:i+min_phrase_length]
                    if all(word not in stop_words for word in phrase):
                        phrases.append(' '.join(phrase))

    # Use the collections.Counter object to count the occurrences of each phrase
    phrase_counts = collections.Counter(phrases)

    # Sort the phrase counts in descending order
    sorted_phrase_counts = sorted(phrase_counts.items(), key=lambda x: x[1], reverse=True)

    # Open the CSV file for writing
    with open(csv_file_phrases, 'w', newline='') as f:
        # Create a CSV writer object
        writer = csv.writer(f)
        # Write the header row
        writer.writerow(['Phrase', 'Count'])
        # Write the data rows
        for phrase, count in sorted_phrase_counts:
            if count > 1:
                writer.writerow([phrase, count])


folder_path = 'files'
csv_file = f'result_words_{timestamp}.csv'
csv_file_phrases = f'result_phrases_{timestamp}.csv'
common_repeated_words(folder_path, csv_file, csv_file_phrases)
print("completed: Saved to " + csv_file)
