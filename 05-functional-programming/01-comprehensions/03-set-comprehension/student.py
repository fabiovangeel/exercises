from movie import movies


def directors(movies):
    return {movie.director for movie in movies}


def common_elements(xs, ys):
    return {y for x in xs for y in ys if x == y}


print(directors(movies))
print(common_elements([1, 2, 4, 6, 8, 10, 12], [1, 4, 8, 12]))
