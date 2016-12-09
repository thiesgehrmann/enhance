from package import *

class samtools(Package):
    fetch="https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2"
    dependencies = ['zlib','ncurses']
    build="make"
    workdir="samtools-1.3.1"

    config =""

    install="""
    make prefix=%(prefix)s install
    """

