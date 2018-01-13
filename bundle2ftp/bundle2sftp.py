import pysftp
import argparse
import os

parser = argparse.ArgumentParser(description='Upload the bundle to the Square 205 SFTP assets folder')
parser.add_argument('-pd','--parentdirectory', type=str, help='the parent directory containg wordpress files')
parser.add_argument('-chd','--childdirectory', type=str, help='designate the theme folder')
args = parser.parse_args()

# SFTP CREDENTIALS
host = ''
pw = ''
user = ''
portnum = 2222

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
bundle_path = f'{os.getcwd()}/{args.parentdirectory}/wordpress/wp-content/themes/{args.childdirectory}/assets/bundle.js'
remote_path = f'/wp-content/themes/{args.childdirectory}/test/'


print('Connecting...')
with pysftp.Connection(host, username=user, password=pw,
                       cnopts=cnopts, port=portnum) as sftp:

    print(f"\nUploading Bundle from: \n{bundle_path}")

    try:
        with sftp.cd(remote_path):
            print('Connected!')
            print(f'Placing file in: {remote_path}...')
            sftp.put(localpath=bundle_path)
            print('\n\nUpload complete!')
    except OSError:
        pass
