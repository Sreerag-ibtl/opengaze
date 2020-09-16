import logging
import argparse

def run(args):
    '''A function that wraps other methods'''
    print(arg)
    
    
if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description = 'Estimate gaze from video')
    parser.add_argument('--src', metavar='-S',
                        type=str, default='0',
                        help='Video file/ camera index')
    parser.add_argument('--dev', metavar='-D',
                        type=bool, default=False,
                        help='Dev mode shows helpful information')
    args = parser.parse_args()
    try:
        run(args)
    except Exception as e:
        logging.info(e)
