from package import *

class augustus(MakePackage):
    dependencies=['bamtools']

    fetch='http://bioinf.uni-greifswald.de/augustus/binaries/augustus.2.7.tar.gz'
    config=""

    build="""
        mkdir -p %(prefix)s/opt/augustus

        sed -i.bak -e 's:INCLUDES = /usr/include/bamtools:INCLUDES = %(prefix)s/includes:' auxprogs/bam2hints/Makefile

        cp -R * %(prefix)s/opt/augustus
        cd %(prefix)s/opt/augustus
       
        make
        """

    install="""
        cd %(prefix)s/opt/augustus
        cp -rs %(prefix)s/opt/augustus/bin/* %(prefix)s/bin/
        cat %(rootpath)s/paths | grep -v AUGUSTUS_CONFIG_PATH > temppath
        echo "export AUGUSTUS_CONFIG_PATH=%(prefix)s/opt/augustus/config" >> temppath
        cp temppath %(rootpath)s/paths
    """ 
