import zipfile
import os

def backupToZip(folder):
    folder = os.path.abspath(folder)
    # find out the expected result zip file name
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # create the zip file
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to tje ZIP file
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done...')


backupToZip('F:\\workspace')
