# Test coverage for PEP-420 packages

```
$ make
coverage run runme.py && coverage report
Name                            Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------------
testme/__init__.py                  0      0      0      0   100%
testme/normal/__init__.py           0      0      0      0   100%
testme/normal/sub/__init__.py       0      0      0      0   100%
testme/normal/sub/testme.py         2      1      0      0    50%   4
---------------------------------------------------------------------------
TOTAL                               2      1      0      0    50%
```

```
$ IMPORT_PEP420=true make
coverage run runme.py && coverage report
Name                            Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------------
testme/__init__.py                  0      0      0      0   100%
testme/normal/__init__.py           0      0      0      0   100%
testme/normal/sub/__init__.py       0      0      0      0   100%
testme/normal/sub/testme.py         2      1      0      0    50%   4
testme/pep420/sub/testme.py         2      1      0      0    50%   4
---------------------------------------------------------------------------
TOTAL                               4      2      0      0    50%
```
