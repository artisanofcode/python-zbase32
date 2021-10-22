"""
zbase32
~~~~~~~

A human-oriented base-32 encoding.
"""

import math
import typing

__all__ = (
    "decode",
    "encode",
    "DecodeError",
)

_ALPHABET = b"ybndrfg8ejkmcpqxot1uwisza345h769"
_INVERSE_ALPHABET = {key: value for value, key in enumerate(_ALPHABET)}


def _chunks(buffer: bytearray, size: int) -> typing.Generator[bytearray, None, None]:
    """
    chunks

    :param buffer: the buffer to chunk
    :param size: the size of each chunk
    :return: an iterable of chunks
    """
    for i in range(0, len(buffer), size):
        yield buffer[i : i + size]


def decode(string: str) -> bytes:
    """
    zbase32 decode

    :param string: a zbase32 encoded string
    :return: decoded bytes

    :raises DecodeError: invalid zbase32 encoded string
    """
    assert isinstance(string, str)

    result = bytearray()

    for chunk in _chunks(bytearray(string.encode()), 8):
        buffer = bytearray(8)

        for index, byte in enumerate(chunk):
            value = _INVERSE_ALPHABET.get(byte, None)

            if value is None:
                raise DecodeError()

            buffer[index] = value

        result.append(((buffer[0] << 3) | (buffer[1] >> 2)) % 256)
        result.append(((buffer[1] << 6) | (buffer[2] << 1) | (buffer[3] >> 4)) % 256)
        result.append(((buffer[3] << 4) | (buffer[4] >> 1)) % 256)
        result.append(((buffer[4] << 7) | (buffer[5] << 2) | (buffer[6] >> 3)) % 256)
        result.append(((buffer[6] << 5) | buffer[7]) % 256)

    length = len(string) * 5 // 8

    return bytes(result[:length])


def encode(data: bytes) -> str:
    """
    zbase32 encode

    :param data: bytes to encode
    :return: a zbase32 encoded string
    """
    assert isinstance(data, bytes)

    result = bytearray()

    for chunk in _chunks(bytearray(data), 5):
        buffer = bytearray(5)

        for index, byte in enumerate(chunk):
            buffer[index] = byte

        result.append(_ALPHABET[((buffer[0] & 0xF8) >> 3)])
        result.append(_ALPHABET[((buffer[0] & 0x07) << 2 | (buffer[1] & 0xC0) >> 6)])
        result.append(_ALPHABET[((buffer[1] & 0x3E) >> 1)])
        result.append(_ALPHABET[((buffer[1] & 0x01) << 4 | (buffer[2] & 0xF0) >> 4)])
        result.append(_ALPHABET[((buffer[2] & 0x0F) << 1 | (buffer[3] & 0x80) >> 7)])
        result.append(_ALPHABET[((buffer[3] & 0x7C) >> 2)])
        result.append(_ALPHABET[((buffer[3] & 0x03) << 3 | (buffer[4] & 0xE0) >> 5)])
        result.append(_ALPHABET[(buffer[4] & 0x1F)])

    length = math.ceil(len(data) * 8.0 / 5.0)

    return bytes(result[:length]).decode()


class DecodeError(RuntimeError):
    """
    zbase32 string cannot be decoded
    """
