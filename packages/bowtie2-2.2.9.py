from package import *

class bowtie2(MakePackage):
    dependencies=["lapack"]

    fetch="http://downloads.sourceforge.net/project/bowtie-bio/bowtie2/2.2.9/bowtie2-2.2.9-source.zip"

    workdir="bowtie2-2.2.9"

    config=""

    build="make"

    install="cp bowtie2-build bowtie2 bowtie2-inspect bowtie2-align-l bowtie2-align-s %(prefix)s/bin"
