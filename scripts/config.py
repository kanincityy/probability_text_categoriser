# config.py

# Define file paths for different newspaper categories
FILE_PATHS = {
    "business": "data/business.txt",
    "sports": "data/sports.txt",
    "technology": "data/technology.txt",
    "politics": "data/politics.txt",
}

# Default probability for unseen words
DEFAULT_PROBABILITY = 1e-6  # Prevents zero probabilities

# Encoding for file reading
ENCODING = "UTF-8"

# Tokenisation regex (word boundaries)
TOKENISATION_REGEX = r"\b\w+\b"
