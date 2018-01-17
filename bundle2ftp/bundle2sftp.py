#!/usr/bin/python3
import argparse
from getpass import getpass
from os import getcwd
import pysftp

parser = argparse.ArgumentParser(description=('Upload the bundle.js to,'
                                              ' the Square 205 SFTP assets folder\n\n A full command Example:'
                                              ' \n "python3 sftp.py -s square205 -st live"'))
parser.add_argument('-st','--state', type=str, help=('State "staging" or "live" as an argument'
                                                     ' to access the staging or live site'))
parser.add_argument('-s','--site', type=str, help=('State the website alias associated'
                                                   'with staging or live site. Ex: "-s square205"'))
parser.add_argument('-a', '--aliases', action='store_true', help=('List avaialbale aliases'))

args = parser.parse_args()
site_alias = args.site
state_alias = args.state
websites = {

    # "alias" : [  "host",
    #              "live site username",
    #              "staging username",
    #              "parent folder/repo name",
    #               "theme folder" name ],

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
        raise SystemExit()

def hostcheck(alias):
    host = websites[alias][0]
    datakey = websites.get(alias, False)[0]

    if datakey == host:
        return websites[alias]
    else:
        print("You've entered an incorrect website alias")
        raise SystemExit()


def aliascheck(request=args.aliases):
    if request == True:
        for i in websites:
            print(f'{i} : {websites[i][0]}')
    else:
        pass
    raise SystemExit()

def main(pword):
    line = "-" * 60
    root = getcwd()
    host = hostcheck(site_alias)
    user = statecheck(state_alias)
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    bundle_path = f'{root}/{host[3]}/wordpress/wp-content/themes/{host[4]}/assets/bundle.js'
    remote_path = f'/wp-content/themes/{host[4]}/assets'

    print(f"\n You've selected: {host[0]}")
    print(line)
    print(f'\n Bundle path: {bundle_path} \n Remote path: {remote_path}')
    print(' '+'~ ' * 10)
    print(f' Host: {host[0]} \n User: {user} \n Password: {pword[0:3]}...\n')
    print(line)
    print('\n\t\t\tConnecting...')

    with pysftp.Connection(host[0], username=user, password=pword,
                           cnopts=cnopts, port=2222) as sftp:

        print('\nConnected!')
        print(f"\n Uploading Bundle from: \n\t{bundle_path}")
        print(f'\n Placing file in: {remote_path}...')

        try:
            with sftp.cd(remote_path):

                sftp.put(localpath=bundle_path)

        except OSError:
            pass

        print('\n\nUpload complete!')

if __name__ == '__main__':

    aliascheck()
    pwprompt = getpass("Please enter the password for the SFTP you wish to access: ")
    main(pwprompt)
