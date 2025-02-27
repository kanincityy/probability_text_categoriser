from collections import defaultdict
import re
import scripts.config as config  # Import configuration file

def read_all_lines(file_path: str) -> list[str]:
    """
    Reads all lines from a file, removing leading/trailing spaces and newline characters.

    Args:
        file_path (str): Path to the file to be read.

    Returns:
        list[str]: A list of cleaned lines from the file.
    """
    with open(file_path, "r", encoding=config.ENCODING) as read_file:  # Use config.ENCODING
        return [line.strip() for line in read_file]  

def tokenise(s: str) -> list[str]:
    """
    Tokenises a string into words by removing punctuation and converting to lowercase.

    Args:
        s (str): The input string.

    Returns:
        list[str]: A list of tokenised words.
    """
    return re.findall(config.TOKENISATION_REGEX, s.lower())  # Use config.TOKENISATION_REGEX

def compute_counts(file_paths: dict) -> dict:
    """
    Computes word frequency counts for each category in the dataset.

    Args:
        file_paths (dict): A dictionary where keys are categories and values are file paths.

    Returns:
        dict: A nested dictionary where counts[category][word] gives the word frequency in that category.
    """
    counts = defaultdict(lambda: defaultdict(int))  # Auto-initialises missing keys

    for category, file_path in file_paths.items():
        file_lines = read_all_lines(file_path)

        for line in file_lines:
            word_list = tokenise(line)

            for word in word_list:
                counts[category][word] += 1  # Automatically increments

    return dict(counts)  # Convert defaultdict to a regular dict for consistency

def compute_probabilities(counts: dict) -> dict:
    """
    Computes the probability P(word | category) for each word in each category.

    Args:
        counts (dict): A nested dictionary where counts[category][word] represents word frequency.

    Returns:
        dict: A nested dictionary where probs[category][word] gives P(word | category).
    """
    probs = {}

    for category, word_counts in counts.items():
        total_words = sum(word_counts.values())

        # Avoid division by zero in case of an empty category
        if total_words == 0:
            probs[category] = {word: config.DEFAULT_PROBABILITY for word in word_counts}  # Use config.DEFAULT_PROBABILITY
        else:
            probs[category] = {word: word_counts[word] / total_words for word in word_counts}

    return probs

# Compute probabilities
counts = compute_counts(config.FILE_PATHS)  # Use config.FILE_PATHS
probs = compute_probabilities(counts)

# Example output
print(f"Probability of 'the' given the category 'business': {probs['business'].get('the', 0.0):0.4f}")