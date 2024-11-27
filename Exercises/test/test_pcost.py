import src.pcost as sut


def test_pcost():
    actual = sut.main("../Data/portfolio.dat")
    expected = 44671.15

    assert actual == expected
