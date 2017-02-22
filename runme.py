import os

if os.environ.get('IMPORT'):
    from testme.normal.sub import testme
    from testme.pep420.sub import testme
