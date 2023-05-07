from PIL import Image
import argparse
import os

if __name__ == '__main__':
    '''Script to help resize an image from the command line.
        usage: resize-image.py [-h] -f FILE -s SIZE SIZE [-v]  

        options:
        -h, --help                        show this help message and exit
        -f FILE, --file FILE              the path to the image you want to resize
        -s SIZE SIZE, --size SIZE SIZE    the size you want to resize the image to, e.g. 400 400
        -v, --verbose    
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True)
    parser.add_argument('-s', '--size', required=True, nargs=2, type=int)
    parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()
    path = os.path.abspath(args.file) # get the absolute file path - not sure if required

    if args.verbose:
        print(f"creating new image of size {args.size} for {args.file}")

    image = Image.open(path)
    image.thumbnail(args.size)
    old_path, ext = path.split('.')
    updated_old_path = f'{old_path}_OLD.{ext}' # create string to update old image name

    if args.verbose:
        print(f'renaming old image from {path} to {updated_old_path}')
        print(f'saving new image at: {args.file}')
    os.rename(path, updated_old_path)
    image.save(args.file)
