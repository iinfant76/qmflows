from pymonad import curry
from qmworks.utils import (chunksOf, concat, concatMap, flatten, zipWith,
                           zipWith3)


def test_chunksOf():
    """
    chunksOf([0, 1, 2, 3], 1) == [[0], [1], [2], [3]]
    """
    assert list(chunksOf([0, 1, 2, 3], 1)) == [[0], [1], [2], [3]]


def test_concat():
    """
    Test list concatenation
    """
    xss = [[1], [2]]
    assert concat(xss) == [1, 2]


def test_concatMap():
    """
    concatMap f == concat (map f)
    """
    f = lambda x: [x * 2]
    xs = [1, 2]
    assert concatMap(f, xs) == list(concat(map(f, xs)))


def test_flatten():
    """
    Concatenation of arrays
    """
    assert flatten(["I\'m", " a", " sentence"]) == "I\'m a sentence"


def test_zipwith():
    """
    zipWith f xs ys ==  map (f) (zip  xs ys)
    """
    @curry
    def f(x, y):
        return  x * y

    xs = range(3)
    ys = range(3, 6)

    assert zipWith(f)(xs)(ys) == [f(x, y) for (x, y) in zip(xs, ys)]


def test_zipwith3():
    """
    zipWith f xs ys zs ==  map (f) (zip  xs ys zs)
    """
    @curry
    def f(x, y, z):
        return  x * y + z

    xs = range(3)
    ys = range(3, 6)
    zs = range(6, 9)

    assert zipWith3(f)(xs)(ys)(zs) == [f(x, y, z) for (x, y, z) in zip(xs, ys, zs)]
