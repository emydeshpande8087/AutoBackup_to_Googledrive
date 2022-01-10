import os
import time
import pprint
upload_status = dict()


def start_listening(source_path):
    while True:
        epoch_seconds = time.time()
        print('epoch', epoch_seconds)
        # print('-----------Files Present in the directory are ----------')
        for dirname, subdir, files in os.walk(source_path):
            for eachfile in files:
                # print(os.path.join(dirname, eachfile))
                # print('Ctime is ', os.stat(os.path.join(dirname, eachfile)).st_ctime)

                if (((epoch_seconds - os.stat(os.path.join(dirname, eachfile)).st_mtime)) < 10):
                    print((epoch_seconds - os.stat(os.path.join(dirname, eachfile)).st_ctime))
                    print('Detected a new file : ', eachfile)
                    upload_status[os.path.join(dirname, eachfile)] = "True"
                else:
                    upload_status[os.path.join(dirname, eachfile)] = "False"
        time.sleep(5)
        pprint.pprint(upload_status)
