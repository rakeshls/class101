import dropbox
class  TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AyETyNBv-pE4vpQKpCPTc8nhgdKw1BR2VRjo2N7moQxb9kC7XFkOhkWn-u_WtTb8Er3ZJXPaVx8uVWYOFINI_wzd-NfDoT2v54ixXQi81-H6QH8FpBD4-avJnh7-_fQyZsD4hKc'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print('file has been moved')
