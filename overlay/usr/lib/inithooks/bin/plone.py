#!/usr/bin/python3
"""Set Plone initial admin password

Option:
    --pass=     unless provided, will ask interactively
"""

import sys
import getopt
import subprocess

from libinithooks.dialog_wrapper import Dialog

DEFAULT_DOMAIN = "www.example.com"


def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print("Syntax: %s [options]" % sys.argv[0], file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)


def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass='])
    except getopt.GetoptError as e:
        usage(e)

    user = ''
    password = ''
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Plone Password",
            "Enter new password for the Plone 'admin' account.")

    subprocess.run(['/usr/lib/inithooks/bin/plone_util.py', password])


if __name__ == "__main__":
    main()
