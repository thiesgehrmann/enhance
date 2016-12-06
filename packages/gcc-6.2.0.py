from package import *
class gcc(MakePackage):
    dependencies=['mpc','mpfr','gmp', 'isl']
    modify_environ={'LIBRARY_PATH':''}

    fetch='ftp://ftp.nluug.nl/mirror/languages/gcc/releases/gcc-%(version)s/gcc-%(version)s.tar.gz'
    workdir="gcc-%(version)s/build"
    config="../configure --prefix=%(prefix)s --with-isl=%(prefix)s -with-mpc=%(prefix)s --with-mpfr=%(prefix)s -with-gmp=%(prefix)s --disable-multilib --disable-libstdcxx-pch"
    
