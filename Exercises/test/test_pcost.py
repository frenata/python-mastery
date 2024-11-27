import src.pcost as sut


def test_basic():
    actual = sut.main("../Data/portfolio.dat")
    expected = 44671.15

    assert actual == expected

def test_extrawhitespace():
    actual = sut.main("../Data/portfolio2.dat")
    expected = 19908.75

    assert actual == expected

