from movie import movies
from util import Card


def genres(movies):
    return {genre for movie in movies for genre in movie.genres}


def actors(movies):
    return {actor for movie in movies for actor in movie.actors}


def repeat_consecutive(xs, n):
    return [i for i in xs for y in range(n)]


def repeat_alternating(xs, n):
    return [i for y in range(n) for i in xs]


def cards(values, suits):
    return {Card(value, suit) for value in values for suit in suits}


print(genres(movies))
print(actors(movies))
print(repeat_consecutive([1, 2, 3], 4))
print(repeat_alternating([1, 2, 3], 4))
print(cards([2, 5, 10], ['hearts', 'diamonds']))
