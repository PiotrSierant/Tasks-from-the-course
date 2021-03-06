import requests
import os
import shutil

def save_url_to_file(url, file_path):

    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)

url = 'sdaasx'
dir = r'E:\dzd07'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path):
        print('Removing {}'.format(tmpfile_path))
        os.remove(tmpfile_path)

    print('Downloading url {}'.format(url))
    save_url_to_file(url, tmpfile_path)

    print('Copying file {} {}'.format(tmpfile_path, file_path))
    shutil.copy(tmpfile_path, file_path)


except requests.exceptions.ConnectionError:
    print('ten błąd łatwo sprowokujesz wpisując nieprawidłowy adres URL {}'.format(e))

except PermissionError:
    print('ten błąd uzyskasz zaznaczając atrybut "tylko do odczytu" dla pliku spis.html{}'.format(e))

except FileNotFoundError:
    print('może się pojawić w trakcie prób, gdy plik download.tmp nie będzie istniał, a wykonywać będzie się instrukcja kopiowania plików{}'.format(e))

except Exception as e:
    print('Error downloading the URL {}'.format(url))
    print('Error details: {}'.format(e))

else:
    print('URL downloaded successfully {}'.format(file))

finally:
    if os.path.exists(tmpfile_path):
        print('Final removal of the file {}'.format(tmpfile_path))
        os.remove(tmpfile_path)
    print('DONE!')