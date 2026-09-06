class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {c: i for i, c in enumerate(order)}

        def convert(word):
            return [alphabet[c] for c in word]

        return words == sorted(words, key=convert)
