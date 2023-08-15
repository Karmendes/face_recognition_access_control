from library.faceRecognition.ageitgey.searcher.main import PersonSearcher
import face_recognition

class Comparer(PersonSearcher):
    def __init__(self):
        pass
    def search(self,encodings,know_encodings):
        names = []
        name = "Unknown"
        for encoding in encodings:
            matches = face_recognition.compare_faces(know_encodings['encodings'],encoding)
            if True in matches:
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}
                for i in matchedIdxs:
                    name = know_encodings["names"][i]
                    counts[name] = counts.get(name, 0) + 1
                    name = max(counts, key=counts.get)
            names.append(name)
        if len(names) > 0:
            return names[0]
        else:
            return name