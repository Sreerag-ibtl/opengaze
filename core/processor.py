from core.gazeutils import GazeDetector

class Process:
    def __init__(self, cam, mode):
        '''
        Running in dev mode or not.
        '''
        self.mode = mode
        self.cam = cam

        self.gaze = GazeDetector()
        
    def __call__(self):
        '''
        Main function processing frame.
        '''
        ok, frame = self.cam.read()
        if not ok:
            return ok, frame
        else:
            if self.mode:
                print('Shape of the frame is {0}'.format(frame.shape))
            frame = self.gaze(frame)
            return ok, frame
