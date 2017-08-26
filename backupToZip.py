#! python3

import zipfile, os

def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    print('Creating %s...' %(zipFilename))
    backupToZip = zipfile.ZipFile(zipFilename, 'w')
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...'%(foldername))
        backupToZip.write(foldername)
#Add all the files in this folder to the ZIP file.
    for filename in filenames:
        newBase = os.path.basename(folder)+'_'
        if filename.startswith(newBase) and filename.endswith('.zip'):
            continue
        backupToZip.write(os.path.join(foldername, filename))
    backupToZip.close()
    print('Done.')

backupToZip('/home/pi/mygit/TIL/Python')

