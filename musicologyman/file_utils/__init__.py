import base64 
from functools import partial
from typing import Sequence,Union
from toolz.functoolz import pipe

def read_all_lines(file_name:str, encoding="utf-8") -> Sequence[str]:
    """Reads all the lines in a text file 

       Returns a list of strings omitting the trailing lines breaks.
    """

    with open(file_name, mode="r", encoding=encoding) as fp:
        return [line[:-1] for line in fp]

def read_all_text(file_name:str, encoding="utf-8") -> str:
    """ Reads a text file and returns its content as a string"""

    with open(file_name, mode="r", encoding=encoding) as fp:
        return fp.read()

def read_binary_file(file_name:str) -> bytes:
    """Reads a binary file and returns its content as a bytes object"""

    with open(file_name, mode="rb") as fp:
        return fp.read()

def write_binary_file(file_name:str, content:Union[bytes,bytearray]) -> None:
    """Write binary content to a a file"""

    with open(file_name, mode="wb") as fp:
        fp.write(content)

def to_base64_string(data:Union[bytes,bytearray], encoding="ascii") -> str:
    return pipe(data, 
                base64.b64encode, 
                partial(bytes.decode,encoding=encoding))

def from_base64_string(base64_str:str, encoding="ascii") -> bytes:
    return pipe(base64_str,
                partial(str.encode,encoding=encoding),
                base64.b64decode)

def read_base64_contents(file_name:str, encoding="ascii") -> bytes:
    """Read a file containing a base64 encoded string and return bytes."""
    
    return pipe(read_all_text(file_name, encoding), 
                from_base64_string)

def write_base64_contents(file_name:str, contents:Union[bytes, bytearray], 
                          encoding="ascii") -> None:
    """Encode binary data as base64 encoded string and write to file."""

    encoded_contents_str = pipe(contents, 
                                to_base64_string, 
                                partial(bytes.decode, encoding=encoding))

    write_text_file(file_name, encoded_contents_str)

