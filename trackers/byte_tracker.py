import supervision as sv
from interfaces.i_object_tracker import IObjectTracker

class ByteTracker(IObjectTracker):
    def __init__(self):
        self.tracker = sv.ByteTrack()
        
    def track(self, detections):
        tracks = {
            "players": [],
            "referees": [],
            "ball": []
        }
        
        for frame_num, detection in enumerate(detections):
            cls_names = detections.names
            cls_names_inv = {v:k for k,v in cls_names.items()}

            detection_supervision = sv.Detections.from_ultralytics(detections)

            # convert goal keeper to player object
            for object_ind, class_id in enumerate(detection_supervision.class_id):
                if cls_names[class_id] == "goalkeeper":
                    detection_supervision.class_id[object_ind] = cls_names_inv["player"]

            detection_with_tracks = self.tracker.update_with_detections(detection_supervision)

            tracks["players"].append({})
            tracks["referees"].append({})
            tracks["ball"].append({})

            for frame_detection in detection_with_tracks:
                bbox = frame_detection[0].tolist()
                cls_id = frame_detection[3]
                track_id = frame_detection[4]

                if cls_id == cls_names_inv['player']:
                    tracks["players"][frame_num][track_id] = {"bbox":bbox}
                
                if cls_id == cls_names_inv['referee']:
                    tracks["referees"][frame_num][track_id] = {"bbox":bbox}

        return tracks 