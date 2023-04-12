import string
import sys

def text_analyzer(text=None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if text is None:
        text = input("What is the text to analyze?\n")
    elif not isinstance(text, str):
        print("AssertionError: argument is not a string")
        return

    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    punct_count = sum(1 for c in text if c in string.punctuation)
    space_count = sum(1 for c in text if c.isspace())

    total_count = len(text)
    print(f"The text contains {total_count} character(s):")
    print(f"- {upper_count} upper letter(s)")
    print(f"- {lower_count} lower letter(s)")
    print(f"- {punct_count} punctuation mark(s)")
    print(f"- {space_count} space(s)")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        text_analyzer()
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        print("Error: this program takes only one argument.")

