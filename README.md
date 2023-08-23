## Inverted_Index
implementation of an inverted index for text documents using NLTK

This Python script demonstrates the creation and usage of an inverted index for a collection of text documents. An inverted index is a data structure commonly used in information retrieval systems to efficiently store and retrieve text-based information.

- Performs text preprocessing, including tokenization, punctuation removal, stopword removal, and lemmatization.
- Uses the Natural Language Toolkit (NLTK) library for text processing tasks.

# Getting Started

1. **Prerequisites:** Ensure you have Python and the NLTK library installed.
   
   ```bash
   pip install nltk
   
2. Clone the Repository: Clone this repository to your local machine.
   ```bash
   git clone https://github.com/your-username/text-inverted-index.git
   cd text-inverted-index
   
3. Download NLTK Resources: Uncomment the required NLTK resource downloads in the code if they are not already downloaded. (Note: If you've already downloaded them, no action is needed.)

4. Replace Document Files: Place your text document files (e.g., doc1.txt, doc2.txt, etc.) in the designated directory.

5. Run the Script: Execute the script main.py to create an inverted index and perform a sample query.
    ```bash
   python main.py

6. Customize and Query: Modify the run_query method in the InvIndex class to perform custom queries on the created inverted index.

# Code Overview
main.py: The main script that imports the necessary modules, defines the InvIndex class, reads document files, creates an instance of InvIndex, and performs a sample query.
funcs.py: Contains the functions for text preprocessing, such as punctuation removal and stopwords handling.
docs/: A directory to place your text document files.
Contributing
Contributions are welcome! If you have ideas for improvements, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
