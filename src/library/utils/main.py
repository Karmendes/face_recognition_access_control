def biggest_area(coords):
    biggest_area = 0
    biggest_coord = None

    for x, y, w, h in coords:
        area = w * h
        if area > biggest_area:
            biggest_area = area
            biggest_coord = (x, y, w, h)

    return biggest_coord
def crop_frame(frame,coord):
        X, Y, W, H = coord
        return frame[Y:Y+H, X:X+W]