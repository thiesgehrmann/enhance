from package import *


class fastqc(Package):
    fetch="http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip"
    workdir='FastQC'    

    build="""
    mkdir -p %(prefix)s/opt/fastqc
    cp -R * %(prefix)s/opt/fastqc
    """

    install="""
    cd %(prefix)s/opt/fastqc 
    sed -i.bak -e 's:^#!/usr/bin/perl$:#!/usr/bin/env perl:' %(prefix)s/opt/fastqc/fastqc
    chmod +x fastqc
    ln -f -s %(prefix)s/opt/fastqc/fastqc  %(prefix)s/bin/
    """

