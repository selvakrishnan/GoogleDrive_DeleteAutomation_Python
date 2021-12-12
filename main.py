from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': 'trashed=false'}).GetList()

for file in file_list:
    if(file['title']=='files_to_delete_list.txt'):
        file = drive.CreateFile({'id': file['id']})
        file.GetContentFile('files_to_delete_list.txt')

with open("files_to_delete_list.txt", "r") as myfile:
	lines = myfile.readlines()

#file_search will search for the file which is mentioned in the files_to_delete_list in the Google Drive
#file_to_be_deleted will contain the files to be deleted
for file_search in file_list:
    for files_to_be_deleted in lines:
        rm = files_to_be_deleted.strip()
        if(file_search['title']==rm):
            ftb = drive.CreateFile({'id': file_search['id']})
            ftb.Delete()




