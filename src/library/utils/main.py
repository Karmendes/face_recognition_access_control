import os
import pickle

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


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")

def save_encodings(encodings,names,name):
    data = {"encodings": encodings, "names": names}
    f = open(f'users/{name}/{name}.pickle', "wb")
    f.write(pickle.dumps(data))
    f.close()

def open_encodings():
    data = {'encodings':[],'names':[]}
    files = [f for f in os.listdir('users') if os.path.isfile(os.path.join('users', f))]
    for file in files:
        path = os.path.join('users', file)
        data.extends(pickle.loads(open(path, "rb").read()))
    return data