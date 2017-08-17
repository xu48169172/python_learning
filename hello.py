#!/usr/bin/env python
import rpm
import os
import sys

ts = rpm.TransactionSet()
fd = os.open(sys.argv[1], os.O_RDONLY)
h = ts.hdrFromFdno(fd)
os.close(fd)

# for dep in h[rpm.RPMTAG_REQUIRENAME]:
#        print dep

for dep in h[rpm.RPMTAG_FILEPROVIDE]:
        print dep
