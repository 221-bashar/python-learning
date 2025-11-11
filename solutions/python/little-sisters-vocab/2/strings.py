"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
             prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
    by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = vocab_words[0]
    words = vocab_words[1:]

    # Use a list comprehension to apply the prefix to every word
    prefixed_words = [prefix + word for word in words]

    # Combine the original prefix and the new prefixed words, then join with ' :: '
    return " :: ".join([prefix] + prefixed_words)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    if word.endswith("ness"):
        # remove 'ness'
        root = word[:-4]
        
        # spelling rule: if word ends with 'i', change to 'y'
        if root.endswith("i"):
            root = root[:-1] + "y"
            
        return root
        
    return word

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    selected_word = sentence.split()[index]
    
    # 2. Clean the word (remove any trailing punctuation)
    cleaned_word = selected_word.rstrip('.,!?"')
    
    # 3. Append the suffix 'en'
    suffix = "en"
    
    # 4. Return the new verb
    return cleaned_word + suffix
