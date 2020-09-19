def run(args):
    '''A function that wraps other methods'''
    src = args.src
    dev = args.dev

    cam = getCamera(src)
    process = Process(cam, dev)
    while True:
        start = time.time()
        ok, frame = process()
        end = time.time()
        if dev:
            print('Processing time : {0} S'.format(end-start))
            print('Approximate FPS : {0} FPS'.format(int(1/(end-start))))
        if not ok:
            if dev:
                print('Error reading camera')
        cv2.imshow('Processed', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':

    try:
        import logging
        import argparse
        from distutils.util import strtobool
        from camutils.util import getCamera
        from core.processor import Process
        import cv2
        import time

        parser = argparse.ArgumentParser(
        description = 'Estimate gaze from video')
        parser.add_argument('--src', metavar='-S',
                            type=str, default='0',
                            help='Video file/ camera index')
        parser.add_argument('--dev', metavar='-D',
                            type=lambda x:bool(strtobool(x)), default=False,
                            help='Dev mode shows helpful information')
        args = parser.parse_args()
        
        run(args)
    except Exception as e:
        #logging.info(e)
        raise e
