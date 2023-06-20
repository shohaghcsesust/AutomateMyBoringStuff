import zipfile
import os


def backup_to_zip(source_directory, target_directory):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    folder = os.path.abspath(source_directory)
    # find out the expected result zip file name
    number = 1
    while True:
        zip_filename = target_directory + "\\" + os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number = number + 1

    # create the zip file
    print('Creating %s...' % zip_filename)
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # walk the entire folder tree and compress the files in each folder
    for folder_name, sub_folders, filenames in os.walk(folder):
        print('Adding files in %s...' % folder_name)
        # Add the current folder to tje ZIP file
        backup_zip.write(folder_name)

        # Add all the files in this folder to the ZIP file
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue  # don't backup the backup ZIP files
            backup_zip.write(os.path.join(folder_name, filename))
    backup_zip.close()
    print('Done...')


directory = 'D:\\shohagh\\workspace\\com\\shohagh\\automate\\apps'
backup_to_zip(directory + '\\source_folder', directory + '\\target_folder')