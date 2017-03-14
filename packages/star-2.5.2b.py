
from package import *

class star(MakePackage):
    fetch="https://github.com/alexdobin/STAR/archive/2.5.2b.tar.gz"
    workdir="STAR-2.5.2b/source"
    config=""
    install="cp STAR %(prefix)s/bin/"


