import shutil
import re
import zipfile
import py7zr
import os
import sys
from pathlib import Path
from unicodedata import normalize, is_normalized

# Загальний список файлів
rez = list()
#Список відсортованих файлів
res_files = list()

# Списки суфіксів для сортування
list_img = ['.JPEG', '.jpeg', '.PNG', '.png',
'.JPG', '.jpg', '.SVG', '.svg']
list_archives = ['.rar', '.RAR', '.zip', '.ZIP',
'.gz', '.GZ', '.tar', '.TAR', '.7z', '.7Z']
list_videos = ['.AVI', '.avi', '.MP4', '.mp4',
'.MOV', '.mov', '.MKV', '.mkv']
list_documents = ['.DOC', '.doc', '.DOCX', '.docs',
 '.TXT', '.txt','.PDF', '.pdf', '.XLSX', '.xlsx', 
'.PPTX', '.pptx', '.xml', '.XML']
list_musics = ['.MP3', '.mp3', '.OGG', '.ogg', 
'.WAV', '.wav', '.AMR', '.amr']

#Бібліотека суфіксів для сортування
dict_suffix ={
                  'images':list_img, 
                  'archives':list_archives, 
                  'videos':list_videos, 
                  'musics':list_musics,
                  'documents': list_documents
                  }

# Списки знайдених суфіксів
suffix_images = set()
suffix_archives = set()
suffix_videos = set()
suffix_documents = set()
suffix_musics = set()
suffix_other = set()

# Бібліотека знайдених суфіксів
dict_suffix_res = {'suffix_images': suffix_images, 'suffix_archives': suffix_archives,
                   'suffix_videos': suffix_videos, 'suffix_documents': suffix_documents,
                   'suffix_musics': suffix_musics, 'suffix_others': suffix_other
                   }

# Списки відсортованих файлів
res_images = []
res_archives = []
res_videos = []
res_documents = []
res_musics = []
res_others = []

#Бібліотека відсортованих файлів
dict_sorting_files = {'res_images': res_images, 'res_archives': res_archives,
                      'res_videos': res_videos, 'res_documents': res_documents,
                      'res_musics': res_musics, 'res_others': res_others
                     }


# Нормалізуємо назву файлу
def normalize_file(name_file):
    new_name_file = normalize('NFC', name_file)
    shutil.move(name_file, new_name_file)


# Аналіз папки з файлами та ігнорування папок якщо в назві міститься "sorted"+ нормалізація
def analiz_files(path_file):
    for i in os.listdir(path_file):
        if is_normalized('NFC', i) == False:
            print('Normalize the file name ', i)
            normalize(i)
        adres_string = str(Path(path_file + '\\' + i))

        if re.search('sorted', adres_string) == None:
            if os.path.isdir(path_file + '\\' + i):

                analiz_files(path_file + '\\' + i)
            else:
                rez.append(adres_string)

    return rez


# Створюємо папку для відсортованих файлів
def create_folder(path_folder, name_folder):
    new_folder = Path(path_folder) / name_folder
    if not Path.exists(new_folder):
        Path.mkdir(new_folder)
    return new_folder


# Складаємо список знайдених суфіксів, та файлів
def create_list_suffix():
    
    for j in rez:
        res_search = False
        for k,i in dict_suffix.items():
            for y in i:
                if Path(j).suffix == y:
                    name_key = 'suffix_'+k
                    name_key1 = 'res_'+k
                    dict_suffix_res[name_key].add(Path(j).suffix)
                    dict_sorting_files[name_key1].append(Path(j))
                    res_search = True

        if res_search == False:
            dict_suffix_res['suffix_others'].add(Path(j).suffix)
            dict_sorting_files['res_others'].append(Path(j))
            search = False                         


# Переносимо файли у відповідні папки
def move_files(res_files, folder_move):
    for file_res in res_files:
        shutil.move(file_res, folder_move)


# Розпаковуємо архіви, якщо вони є, та видаляємо самі архіви після розпакування
def unpack_archive(dyrectory_for_inpack):
    try:
        folder_archive = dyrectory_for_inpack + '\\archives_sorted'
        for archive in os.listdir(folder_archive):
            if Path(archive).suffix == '.zip' or Path(archive).suffix == '.tar' or Path(archive).suffix == '.gz':
                file_for_unpack = zipfile.ZipFile(
                    folder_archive + '\\'+archive)
                file_for_unpack.extractall(folder_archive)
                file_for_unpack.close()
                root_for_delete = Path(folder_archive + '\\'+archive)
                try:
                    Path.unlink(root_for_delete)
                except OSError as e:
                    print("Error: %s : %s" % (root_for_delete, e.strerror))

            elif Path(archive).suffix == '.7z':
                path_archive = folder_archive+'\\' + archive
                file_for_unpack = py7zr.SevenZipFile(path_archive, mode='r')
                file_for_unpack.extractall(
                    folder_archive + '\\' + Path(archive).stem)
                file_for_unpack.close()
                root_for_delete = Path(folder_archive + '\\'+archive)
                try:
                    Path.unlink(root_for_delete)
                except OSError as e:
                    print("Error: %s : %s" % (root_for_delete, e.strerror))
    except:
        print('Archives for unpacking not found')


# Працюємо зі знайденими файлами та розширеннями (виводимо список, переносимо у відповідні папки)
def report_and_create_folder(dyrectory):
    for k, v in dict_suffix_res.items():
        if len(v)>0:
            print(f'Found suffixes {k[7:]}:')
            for t in v:
                print(t)
            new_folder = create_folder(dyrectory, k[7:]+'_sorted')
            print(f'Found files {k[7:]}:')
            for k1 in dict_sorting_files['res_'+k[7:]]:
                print(Path(k1).name)
                res_files.append(Path(k1))                        
            move_files(res_files, new_folder)
            res_files.clear()    

# Видаляємо пусті папки з-під файлів
def delete_empty_folder(path_for_delete):
    try:
        for i in os.listdir(path_for_delete):
            adres_path = Path(path_for_delete + '\\' + i)
            if re.search('sorted', str(adres_path)) == None:
                try:
                    shutil.rmtree(adres_path)
                except OSError as e:
                    print("Error: %s : %s" % (str(adres_path), e.strerror))
    except:
        print('Folders to delete not found')


# Головна процедура для проведення розбору файлів
def main():
    path_for_analize = input('Enter the full path to the folder >>>> ')
    try:
        dyrectory_current = path_for_analize
        analiz_files(dyrectory_current)
        create_list_suffix()
        report_and_create_folder(dyrectory_current)
        unpack_archive(dyrectory_current)
        delete_empty_folder(dyrectory_current)
        query = input('Want to repeat with another folder ? (yes/no)\n>>>> ')
        if query.lower() == 'yes':
            main()
    except:
        print('Enter the path to the folder')


if __name__ == '__main__':
    main()


