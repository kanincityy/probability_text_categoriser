def compute_smoothed_probabilities(counts: dict) -> dict:
    """
    Computes smoothed probabilities P(word | category) for each word in each category.

    Args:
        counts (dict): A nested dictionary where counts[category][word] represents word frequency.

    Returns:
        dict: A nested dictionary where probs[category][word] gives smoothed P(word | category).
    """
    # Set of unique words across all categories
    unique_words = set()
    for cat in counts:
        unique_words.update(counts[cat].keys())

    # Total number of unique words
    total_unique_words = len(unique_words)
    probs = {}

    # Iterate through categories and words to compute smoothed probabilities
    for category, words in counts.items():
        probs[category] = {}
        total_words_category = sum(words.values())  # Total word count in the category

        # Smoothing: Add 1 to every word count
        for word in unique_words:
            # P(word | category) = (count(word, category) + 1) / (total words in category + total unique words)
            probs[category][word] = (words.get(word, 0) + 1) / (total_words_category + total_unique_words)

    return probs

import math

def categorise_text_v2(text, prob_category, smoothed_prob_category_word):
    """
    Categorises a given text based on the highest log probability of belonging to a category.

    Args:
        text (str): The text to be categorised.
        prob_category (dict): A dictionary of prior probabilities for each category.
        smoothed_prob_category_word (dict): A nested dictionary of smoothed word probabilities for each category.

    Returns:
        str: The predicted category for the text.
    """
    words = tokenise(text)  # Tokenise the text into words
    p_cat_text = {}  # Store the log probabilities for each category

    # Iterate through each category to calculate the log probability
    for category in prob_category:
        log_prob = math.log(prob_category[category])  # Start with the log of the prior probability

        # Add log probabilities for each word in the text
        for word in words:
            if word in smoothed_prob_category_word[category]:
                log_prob += math.log(smoothed_prob_category_word[category][word])
            else:
                log_prob += -math.inf  # If the word isn't in the category, assign negative infinity to avoid it influencing the result

        p_cat_text[category] = log_prob  # Store the log probability for the category

    # Return the category with the highest log probability
    return max(p_cat_text, key=p_cat_text.get)
