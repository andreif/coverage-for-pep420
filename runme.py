import os
from testme.normal.sub import testme

if os.environ.get('IMPORT_PEP420'):
    from testme.pep420.sub import testme
