"""
test zbase32
"""

import hypothesis
import hypothesis.strategies
import pytest

import zbase32


@pytest.mark.parametrize(
    ["decoded", "encoded"],
    [
        (b"asdasd", "cf3seamuco"),
        (b"\xF0\xBF\xC7", "6n9hq"),
        (b"\xD4\x7A\x04", "4t7ye"),
        (b"\xff", "9h"),
        (b"\xb5", "sw"),
        (b"\x34\x5a", "gtpy"),
        (b"\xff\xff\xff\xff\xff", "99999999"),
        (b"\xff\xff\xff\xff\xff\xff", "999999999h"),
        (
            b"\xc0\x73\x62\x4a\xaf\x39\x78\x51\x4e\xf8\x44\x3b\xb2\xa8\x59"
            b"\xc7\x5f\xc3\xcc\x6a\xf2\x6d\x5a\xaa",
            "ab3sr1ix8fhfnuzaeo75fkn3a7xh8udk6jsiiko",
        ),
    ],
)
def test_it_should_support_encoding_and_decoding(decoded, encoded) -> None:
    """it should support encoding and decoding."""
    assert zbase32.encode(decoded) == encoded
    assert zbase32.decode(encoded) == decoded


def test_it_should_error_on_invalid_zbase32_strings() -> None:
    """it should error on invalid zbase32 strings."""
    with pytest.raises(zbase32.DecodeError):
        zbase32.decode("bar#")


@hypothesis.given(value=hypothesis.strategies.binary())
def test_it_should_be_able_to_decode_encoded_values(value: bytes) -> None:
    """it should be able to decode encoded values."""
    assert zbase32.decode(zbase32.encode(value)) == value
