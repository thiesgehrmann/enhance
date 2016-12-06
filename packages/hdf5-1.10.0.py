from package import *

class hdf5(MakePackage):
    dependencies = ["zlib"]
    fetch="https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.10/hdf5-1.10.0-patch1/src/hdf5-1.10.0-patch1.tar.gz"
    config="./configure --prefix=%(prefix)s --enable-cxx"

