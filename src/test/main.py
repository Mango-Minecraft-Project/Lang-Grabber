from zipfile import ZipFile
from re import match
from os import mkdir, rename, removedirs
from os.path import isdir

target_filename = 'alloy_forgery.jar'
lang_regex = r'assets\/\w+\/lang\/\w+\.json'

with ZipFile(target_filename) as jar_file:
    print('FIND > lang file:')
    lang_files = []
    for filename in jar_file.namelist():
        if match(lang_regex, filename):
            print(f'\t{filename}')
            lang_files.append(filename)
    namespace = lang_files[0].split('/')[1]
    if not isdir(namespace):
        mkdir(namespace)
    for filename in lang_files:
        jar_file.extract(filename, path=f'./{namespace}')
        rename(f'./{namespace}/{filename}', f'./{namespace}/{filename.split("/")[-1]}')
    removedirs(f'{namespace}/assets/{namespace}/lang')