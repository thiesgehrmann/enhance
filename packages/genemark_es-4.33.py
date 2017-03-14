from package import *

class genemark_es(Package):
    dependencies = ['perl']
    def fetch(self):
        f = self.fillVars('%(srcpath)s/gm_et_linux_64.tar.gz')
        if not os.path.isfile(f):
            error('Please supply source file: %s from http://exon.gatech.edu/GeneMark/license_download.cgi' %f)
        f2 = self.fillVars('%(srcpath)s/gm_key_64.tar')
        if not os.path.isfile(f):
            error('Please supply key file: %s from http://exon.gatech.edu/GeneMark/license_download.cgi' %f)
        return f

    config="""
            cp %(srcpath)s/gm_key_64.gz .
            gunzip gm_key_64.gz
            """

    build="""
        mkdir -p %(prefix)s/opt/genemark_es
        sed -i.bak -e 's:#!/usr/bin/perl:#!/usr/bin/env perl:' `find | grep -e '.pl$'`
        cp -R * %(prefix)s/opt/genemark_es
        cp gm_key_64 $HOME/.gm_key
        cd %(prefix)s/opt/genemark_es
        """

    install="""
        cd %(prefix)s/opt/genemark_es
        ln -f -s %(prefix)s/opt/genemark_es/gmes_petap/gmes_petap.pl %(prefix)s/bin/
        ln -f -s %(prefix)s/opt/genemark_es/gmes_petap/gmhmme3 %(prefix)s/bin/
        ln -f -s %(prefix)s/opt/genemark_es/gmes_petap/probuild %(prefix)s/bin/
        echo "export GENEMARK_PATH=%(prefix)s/bin/gmes_petap.pl" >> %(prefix)s/../paths
    """

