import dropbox
class TransferData:
    def __init__ (self, access_token):
        self.access_token=access_token
    def upload_file (self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)
def main():
    access_token="sl.AwYF5fAk-Y15fuKtwxtewCgkdb1vsM9daNzbuPDgPONrJgOEQ09ta7k5gLWyFQzqAxFTraod-KNDFLOxMYxeTiqH6P_SmZf-ZcAAgC2A5u9JpG1WA_Y-JQyPk3U34_u7sqku-8s"
    transferData=TransferData(access_token)
    file_from=input("Enter the path of the file to transfer")
    file_to="/RomirArya/test.jpeg"
    transferData.upload_file(file_from, file_to)
    print("File has been moved")
main()
