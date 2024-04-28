import pytest

from but_better import parse_youtube_url


@pytest.mark.parametrize(
    "url, expected",
    [
        ("https://www.youtube.com/watch?v=abcdefg", "abcdefg"),
        ("https://www.youtube.com/watch?v=abcdefg&list=abc&index=3", "abcdefg"),
    ],
)
def test_parse_youtube_url(url, expected):
    assert parse_youtube_url(url) == expected
