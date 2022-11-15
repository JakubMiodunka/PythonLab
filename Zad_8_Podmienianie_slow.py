#!/bin/env python3
import argparse

class TextReplace:
    def __init__(self) -> None:
        # Preparing config
        self.CONVERSION_CONFIG = {"i": "oraz",
                                  "oraz": "i",
                                  "nigdy": "prawie nigdy",
                                  "dlaczego": "czemu"
                                 }
        self.SEPARATOR = " "

    def replace(self, text: str) -> str:
        # Splitting given text to words
        words = text.split(self.SEPARATOR)

        # Repleacing words according to self.CONVERSION_CONFIG
        for index, word in enumerate(words):
            if word in self.CONVERSION_CONFIG:
                words[index] = self.CONVERSION_CONFIG[word]

        # Joining words back toghether
        return " ".join(words)
        
    def __call__(self, text: str) -> str:
        return self.replace(text)

if __name__ == "__main__":
    # Parsing text to the script as argument
    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    args = parser.parse_args()

    # Performing replacemant is use of TextReplace class instance
    text_replacemet = TextReplace()
    print(text_replacemet(args.text))

