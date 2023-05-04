# TXT-to-JSON
This Python script converts text files to JSON format with various formatting changes made, including adding an "ArticleHeader" key, bolding specific abbreviations, italicizing paragraphs, and adding indentation to numbered lists. The original files are replaced with the newly formatted JSON files.


Text-to-JSON Converter
This Python script converts a directory of text files to JSON format, with various formatting changes made to the text in the process.

Usage
Download the convert_to_json.py file and save it to a local directory on your computer.

Copy all the text files you want to convert to JSON to a directory on your local computer.

Open a terminal or command prompt window and navigate to the directory where you saved the convert_to_json.py file and the directory with your text files.

Run the following command to install the required regex module:

Copy code
pip install regex
Run the following command to execute the script and convert all the text files to JSON format:

Copy code
python convert_to_json.py
Once the script has finished running, all the original text files will have been replaced with the newly formatted JSON files in the same directory.

Formatting Changes
The script makes the following formatting changes to the text:

Adds an "ArticleHeader" key to the JSON object based on the name of the original text file, with the ".txt" extension removed.
Reformats the first line of each file as an h1 heading.
Bolds specific abbreviations.
Italicizes all paragraphs except those within block quotes or h1 tags.
Adds indentation to numbered lists.
Requirements
Python 3.x
regex module (can be installed via pip)
Contributing
Bug reports and pull requests are welcome on GitHub at https://github.com/example/text-to-json-converter.

License
The script is available as open source under the terms of the MIT License.
