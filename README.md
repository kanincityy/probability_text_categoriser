# Text Categoriser 

This project implements a **text categoriser** that classifies text into predefined categories based on the frequency of words and their probabilities. It uses **Naive Bayes** classification techniques, applying both **smoothed and unsmoothed probabilities** to categorise text documents.

## Project Overview 

The categoriser is designed to work with text data and determines the most likely category for a given text. It calculates the probabilities of words given a category (P(word|category)) and combines them using the **log-probability** approach. The categoriser uses both unsmoothed and smoothed probabilities to improve its accuracy. The model can be used to classify text data into categories like **business, technology, politics**, etc., based on word occurrence patterns.

## Files and Structure 

- `config.py`: Configuration file storing constants such as paths, categories, and smoothing parameters.
- `utils.py`: Utility functions for reading files, tokenising text, and processing word counts.
- `categoriser.py`: Core script containing functions to compute probabilities and categorise text.
- `main.py`: Main entry point that calls the functions and executes the categorisation.

## Features 

- Tokenises text and computes word counts for each category.
- Computes **unsmoothed** and **smoothed probabilities** for words in each category.
- Uses **log-probability** to classify text based on computed probabilities.
- Supports handling of both sparse and dense feature matrices.

## Requirements 

- `math`
- `re`
- `collections`

These are standard Python libraries, so no additional installations are necessary.

## How to Run 

If you'd like to try out the project, follow these steps:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/kanincityy/text_categoriser.git
    ```
2. Navigate to the project's directory.
3. Ensure you have Python installed (Python 3.6 or higher recommended).
4. Run the code in `main.py`:
    ```bash
    python main.py
    ```

## Contributing 

This project is a reflection of my learning, but feel free to fork the repository and contribute if you have ideas or improvements!

## License 

This repository is licensed under the MIT License. See the LICENSE file for details.

---

Happy coding! ✨🐇