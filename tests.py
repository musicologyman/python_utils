import sys
from she_persisted import to_base64_string, from_base64_string

BINARY_TEST_DATA = b'The quick brown fox jumped over the lazy dog' 
BASE64_TEST_DATA = \
    'VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2cu'


def test():
    try:
        assert to_base64_string(BINARY_TEST_DATA) == BASE64_TEST_DATA     
        assert from_base64_string(BASE64_TEST_DATA) == BINARY_TEST_DATA
    except AssertionError:
        print("AssertionError: shit happened")

if __name__ == "__main__":
    test()
      
