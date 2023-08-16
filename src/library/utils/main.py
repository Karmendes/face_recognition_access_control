import os
import pickle
import cv2

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

def save_images(frames,name):
    [cv2.imwrite(f'images/{name}/{x}.png', y) for x,y in enumerate(frames)]


def list_files_with_paths_in_subdirectories(directory):
    file_paths = []
    for root_folder, subfolders, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root_folder, file)  
            file_paths.append(file_path)
    return file_paths

def open_encodings():
    data = {'encodings':[],'names':[]}
    files = list_files_with_paths_in_subdirectories('users')
    for file in files:
        pickle_data = pickle.loads(open(file, "rb").read())
        data['encodings'].extend(pickle_data['encodings'])
        data['names'].extend(pickle_data['names'])
    return data
