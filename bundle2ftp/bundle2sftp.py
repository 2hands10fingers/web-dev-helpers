import pysftp
import argparse
from getpass import getpass
from os import getcwd

parser = argparse.ArgumentParser(description='Upload the bundle to the Square 205 SFTP assets folder')
parser.add_argument('-st','--state', type=str, help='State "staging" or "live" as an argument to access the staging or live site')
parser.add_argument('-s','--site', type=str, help='State "staging" or "live" as an argument to access the staging or live site')
args = parser.parse_args()
site_alias = args.site
state_alias = args.state
websites = {

    # "alias" : [ "host",
    #            "live site username",
    #             "staging username",
    #             "parent folder/repo name",
    #             "theme folder" name ],

    "example" : [   "example.sftp.wpengine.com",
                    "exampl-username-for-live",
                    "example-username-for-staging",
                    "example-reponame",
                    "example-theme-name" ]
}

def statecheck(state):
    stagingsite = websites[site_alias][2]
    livesite = websites[site_alias][1]

    if state.lower() == 'live':
        return livesite
    elif state.lower() == 'staging':
        return stagingsite
    else:
        print ("You've entered an incorrect website state")

def hostcheck(alias):
    host = websites[alias][0]
    datakey = websites.get(alias, False)[0]

    if datakey == host:
        return host
    else:
        print("You've entered an incorrect website alias")

def pfoldercheck(alias):
    pfolder = websites[site_alias][3]
    for i in websites:
        if i == alias:
            return pfolder
        else:
            pass

def chfoldercheck(alias):
    chfolder = websites[site_alias][4]

    for i in websites:
        if i == alias:
            return chfolder
        else:
            pass


root = getcwd()
host = hostcheck(site_alias)
user = statecheck(state_alias)
parentfolder = pfoldercheck(site_alias)
themefolder = chfoldercheck(site_alias)
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
bundle_path = f'{root}/{parentfolder}/wordpress/wp-content/themes/{themefolder}/assets/bundle.js'
remote_path = f'/wp-content/themes/{themefolder}/assets/'

if __name__ == '__main__':

    pwprompt = getpass("Please enter the password for the SFTP you wish to access: ")

    print(f"\nYou've selected {host}")
    print(f'\n Bundle path: {bundle_path} \n Remote path: {remote_path} \n' )
    print(f' Host: {host} \n User: {user} \n Password: {pwprompt[0:2]}...')
    print('\n\t\tConnecting...')

    with pysftp.Connection(host, username=user, password=pwprompt,
                           cnopts=cnopts, port=2222) as sftp:

        try:
            with sftp.cd(remote_path):
                print('\nConnected!')
                print(f"\nUploading Bundle from: \n{bundle_path}")
                print(f'Placing file in: {remote_path}...')
                sftp.put(localpath=bundle_path)
                print('\n\nUpload complete!')
        except OSError:
            pass
