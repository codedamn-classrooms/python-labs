from typing import List
from collections import deque

def word_ladder(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    This function finds the length of the shortest transformation sequence from `beginWord` to `endWord`,
    changing one letter at a time, with each intermediate word being in `wordList`.

    :param beginWord: The word to start the transformation.
    :param endWord: The word to end the transformation.
    :param wordList: A list of allowed words for the transformation.
    :return: The length of the shortest transformation sequence. If no such sequence exists, returns 0.
    """
    pass

# Example calls
print(word_ladder("and", "ant", ["add", "aid", "and", "ant", "any"]))  # Expected output: 1
print(word_ladder("phone", "phase", ["phone", "phane", "plane", "prane", "prase", "phase"]))  # Expected output: 2
