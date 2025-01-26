import mock


def test_tokenize():
    text = "Hello darkness, my old friend\nI've come to talk with you again"
    tokens = [
        "hello",
        "darkness",
        "my",
        "old",
        "friend",
        "i",
        "ve",
        "come",
        "to",
        "talk",
        "with",
        "you",
        "again",
    ]
    assert mock.tokenize(text) == tokens
