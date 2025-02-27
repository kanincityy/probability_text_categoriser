import os
from scripts.config import *  # Importing constants from the config.py file
from scripts.utils import (
    read_all_lines,
    tokenise,
    compute_counts,
    compute_probabilities,
    compute_smoothed_probabilities,
)
from scripts.categoriser import (
    categorise_text,
    categorise_text_v2
)

def main():
    # Example of file paths for each category
    file_paths = {
        "business": "data/business.txt",  # Replace with actual paths
        "sport": "data/sport.txt",        # Replace with actual paths
    }

    # Step 1: Compute word counts for each category
    print("Computing word counts...")
    counts = compute_counts(file_paths)
    print(f"Word counts computed for categories: {counts}")

    # Step 2: Compute probabilities for each word in each category
    print("\nComputing probabilities...")
    probs = compute_probabilities(counts)
    print(f"Probabilities computed for categories: {probs}")

    # Step 3: Compute smoothed probabilities for each word in each category
    print("\nComputing smoothed probabilities...")
    smoothed_probs = compute_smoothed_probabilities(counts)
    print(f"Smoothed probabilities computed for categories: {smoothed_probs}")

    # Step 4: Set up prior probabilities (uniform in this example)
    n_cats = len(probs)
    prob_category = {cat: 1 / n_cats for cat in probs}
    print(f"Prior probabilities for categories: {prob_category}")

    # Step 5: Test categoriser functions with example text
    print("\nTesting categoriser functions...")

    text = "The company is doing a lot of business."
    print(f"Text: {text}")
    category = categorise_text(text, prob_category, probs)
    print(f"Categorised by categorise_text: {category}")

    category_v2 = categorise_text_v2(text, prob_category, smoothed_probs)
    print(f"Categorised by categorise_text_v2: {category_v2}")

    # More test examples
    test_texts = [
        "She is a star.",
        "The prime minister gave a speech today.",
        "A great technological breakthrough in AI.",
        "They came in first place in the competition."
    ]

    for test_text in test_texts:
        print(f"\nTesting text: {test_text}")
        category_v2 = categorise_text_v2(test_text, prob_category, smoothed_probs)
        print(f"Categorised as: {category_v2}")

if __name__ == "__main__":
    main()
