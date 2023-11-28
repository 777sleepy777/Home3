import argparse
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging

parser = argparse.ArgumentParser(description='App for sorting folder')
parser.add_argument('-s', '--source', default='pict') #required=True)
parser.add_argument('-o', '--output', default='dist')
args = vars(parser.parse_args())
source = args.get('source')
output = args.get('output')

folders =[]

def look_over_folder(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            look_over_folder(el)

def copy_file(path: Path):
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix
            new_path = output_folder / ext
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(el,new_path / el.name)
            except OSError as e:
                logging.error(e)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    main_folder = Path(source)
    output_folder = Path(output)

    folders.append(main_folder)
    look_over_folder(main_folder)
    print(folders)
    threads = []
    for folder in folders:
        th = Thread(target=copy_file, args=(folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    print('You can del base folder')























