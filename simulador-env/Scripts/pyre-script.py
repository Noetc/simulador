#!C:\Users\Administrator\github\simulador\simulador-env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pyre-check==0.9.15','console_scripts','pyre'
__requires__ = 'pyre-check==0.9.15'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pyre-check==0.9.15', 'console_scripts', 'pyre')()
    )
