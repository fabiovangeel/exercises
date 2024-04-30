def closest(points, target_point):
    tx, ty = target_point

    def distance(point):
        x, y = point
        x_diff = x - tx
        y_diff = y - ty
        return ((x_diff**2) + (y_diff**2))**0.5

    return min(points, key=distance)
