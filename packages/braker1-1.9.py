from package import *

class braker1(Package):
    dependencies = ['perl', 'genemark_es', 'augustus']

    fetch = "http://exon.gatech.edu/Braker/BRAKER1.tar.gz"

    config = ""

    def install(self):
      c="""
        mkdir -p %(prefix)s/opt/braker1
        sed -i.bak braker.pl -e 's:^#!/usr/bin/perl:#!/usr/bin/env perl:'
        sed -i.bak filterIntronsFindStrand.pl -e 's:^#!/usr/bin/perl:#!/usr/bin/env perl:'
        sed -i.bak filterGenemark.pl -e 's:^#!/usr/bin/perl:#!/usr/bin/env perl:'

        cp ./* %(prefix)s/opt/braker1
        ln -sf %(prefix)s/opt/braker1/braker.pl %(prefix)s/bin/
        ln -sf %(prefix)s/opt/braker1/filterIntronsFindStrand.pl %(prefix)s/bin/
        ln -sf %(prefix)s/opt/braker1/filterGenemark.pl %(prefix)s/bin/ 
        ln -sf %(prefix)s/opt/braker1/helpMod.pm %(prefix)s/bin/

        cpanm Scalar::Util::Numeric
        cpanm Parallel::ForkManager
        cpanm YAML
        cpanm Hash::Merge
        cpanm Logger::Simple
      """
      for cmd in c.split("\n"):
        runCommand(self.fillVars(cmd))
