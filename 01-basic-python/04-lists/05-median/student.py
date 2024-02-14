def median(ns):
    sorted_list = sorted(ns)
    middle = len(ns) // 2
    if len(ns) % 2 == 0:
        return (sorted_list[middle] + sorted_list[middle-1])/2
    else:
        return sorted_list[middle]
