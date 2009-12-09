#!/usr/bin/env python
import os
import struct
import sys
import zipfile

def main():
    if len(sys.argv) != 2:
        print 'Usage', sys.argv[0], '<filename.crx>'
        sys.exit(1)
    f = open(sys.argv[1], 'rb')
    assert (f.read(4) == 'Cr24')
    version = struct.unpack('I', f.read(4))[0]
    key_size = struct.unpack('I', f.read(4))[0]
    sig_size = struct.unpack('I', f.read(4))[0]
    key = f.read(key_size)
    sig = f.read(sig_size)
    print 'PKZip starts at', f.tell()
    zf = zipfile.ZipFile(f)
    print zf.namelist()
    os.mkdir(os.path.basename(sys.argv[1]))
    os.chdir(os.path.basename(sys.argv[1]))
    for filename in zf.namelist():
        if filename.endswith('/'):
            os.mkdir(filename)
            continue
        outfile = open(filename, 'wb')
        outfile.write(zf.read(filename))
        outfile.close()

if __name__ == "__main__":
    main()
