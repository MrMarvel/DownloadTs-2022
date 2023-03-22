import os
import shutil
import urllib.request


def download_ts():
    print('Beginning file download with urllib2...')
    cwd = os.getcwd()  # Get the current working directory (cwd)
    TS_DIR = 'ts_files'
    if not os.path.exists('ts_files'):
        print('ts_file folder is not found, creating the folder.')
        os.makedirs('ts_files')

    url = 'https://events-delivery-files.webinar.ru/streamer/default/storage/events-storage.webinar.ru/api-storage/files/webinar/2022/02/09/45d1cf701ba2c54095600ee4110a88404ae5b1c4a3bd0bfbef4aaa406c8.mp4'
    i = 0
    while True:
        suffix = "media_" + str(i) + ".ts"
        new_url = url + "/" + suffix
        print(f'Downloading #{i} part')
        try:
            urllib.request.urlretrieve(new_url, f'{cwd}/{TS_DIR}/' + suffix)
        except:
            print(f'Error downloading #{i} part')
            break
        i += 1
    print(f'Finished downloading {url}')


def merge_ts():
    print('Merging ts files')
    cwd = os.getcwd()  # Get the current working directory (cwd)
    TS_DIR = 'ts_files'
    TS_DIR_PATH = os.path.join(cwd, TS_DIR)
    with open('merged.ts', 'wb') as merged:
        i = 0
        while True:
            file_name = 'media_' + str(i) + '.ts'
            ts_file = os.path.join(TS_DIR_PATH, file_name)
            print(f'Merging {file_name}')
            try:
                with open(ts_file, 'rb') as mergefile:
                    shutil.copyfileobj(mergefile, merged)
            except:
                print(f'Error merging {file_name}!')
                break
            i += 1

    print('Merged to merged.ts!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # download_ts()
    merge_ts()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
