from pocketbase import PocketBase  # Client also works the same
from pocketbase.client import FileUpload
import os

client = PocketBase('https://animevariant.fly.dev/')

username = os.environ.get('POCKETBASE_USERNAME')
password = os.environ.get('POCKETBASE_PASSWORD')

# or as admin
admin_data = client.admins.auth_with_password(username, password)
# create backup
create = client.backups.create('pb_data.zip')


# # after creating backup is done, you can download it
# token = client.files.getToken()
# download = client.backups.getDownloadUrl(token, 'pb_data.zip')
