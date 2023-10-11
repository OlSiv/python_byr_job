def slices(series, length):

    if series == "":
        raise ValueError("series cannot be empty")

    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")

    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    sp = []
    series_2 = list(series)
    while len(series_2) >= length:
        sp.append(''.join(series_2[0:length]))
        del series_2[0]
    return sp
