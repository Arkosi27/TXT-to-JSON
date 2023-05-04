import os
import re
import json

path = "/Users/henry/Desktop/articles"

def convert_to_json(file_path):
    # Open the file and read its contents
    with open(file_path, 'r') as f:
        text = f.read()

        # Create a dictionary to hold the article data
        article = {}

        # Add the article header to the dictionary
        file_name = os.path.basename(file_path)
        article["ArticleHeader"] = os.path.splitext(file_name)[0]

        # Split the text into paragraphs
        paragraphs = re.split("\n\n+", text)

        # Create a list to hold the formatted paragraphs
        para_list = []

        # Iterate over the paragraphs and format them
        for para in paragraphs:
            # Remove leading and trailing whitespace
            para = para.strip()

            # Skip empty paragraphs
            if not para:
                continue

            # Check if the paragraph is a quote
            if para.startswith(">"):
                # Add the quote formatting
                para = "<blockquote>" + para[1:].strip() + "</blockquote>"
            else:
                # Add italic tags to the paragraph
                para = "<i>" + para + "</i>"
                # Add bold tags to the abbreviations
                para = re.sub(r"\b(Hey[1-3])\.?\s", r"<b>\1.</b> ", para)
                # Add indentation to lines with numbers
                para = re.sub(r"^\d+\.?\s+", r"<indent=15%>", para)
                # Add indentation to lines with numbered parentheses
                para = re.sub(r"\((\d+|\d+\([1-9]\d*\))\)", r"<indent=15%>(\1)</indent>\n", para)

            # Add the paragraph to the list
            para_list.append(para)

        # Add the list of paragraphs to the article
        article["ParagraphStrings"] = para_list

        # Convert the article to JSON
        json_data = json.dumps(article, indent=4)

        # Define the output file name
        output_file = os.path.splitext(file_path)[0] + ".json"

        # Write the JSON data to the output file
        with open(output_file, 'w') as f:
            f.write(json_data)

        # Remove the original text file
        #os.remove(file_path)

# Iterate over the text files in the directory and convert each one to JSON
for file_name in os.listdir(path):
    if file_name.endswith(".txt"):
        file_path = os.path.join(path, file_name)
        convert_to_json(file_path)
