import os
import time

#directory = 'C:\\Project\\testProject_2'
directory  = '.'
path_normalized = os.path.normpath(directory)

for dir_path, dir_names, file_names in os.walk(path_normalized):
    print(dir_path, '\n', dir_names, '\n', file_names)

    for files in file_names:
        filepath = os.path.join(dir_path, files)
        print(filepath)
        print(os.path.dirname(filepath))
        filetimes = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetimes))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {files}, Путь: {filepath},'
              f' Размер: {filesize} байт, Время изменения: {formatted_time},'
              f' Родительская директория: {parent_dir}')
