def get_coordinates(geo_obj):
    ll = [float(v) for v in geo_obj["Point"]["pos"].split(" ")]

    lower_corner = [float(v) for v in geo_obj['boundedBy']['Envelope']['lowerCorner'].split()]
    upper_corner = [float(v) for v in geo_obj['boundedBy']['Envelope']['upperCorner'].split()]
    spn = [upper_corner[0] - lower_corner[0], upper_corner[1] - lower_corner[1]]

    return ll, spn


def get_length(p1x, p1y, p2x, p2y):
    return round(((p1x - p2x) ** 2 + (p1y - p2y) ** 2) ** 0.5 * 111000)
