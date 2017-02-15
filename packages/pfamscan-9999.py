from package import *

class pfamscan(MakePackage):

  dependencies=["bioperl"]

  fetch="ftp://ftp.ebi.ac.uk/pub/databases/Pfam/Tools/PfamScan.tar.gz"
  workdir="PfamScan"
  config=""
  build=""
  def install(self):
    c="""pwd
         cpan Moose
         mkdir -p %(prefix)s/opt/pfamscan
         cp ./* -r %(prefix)s/opt/pfamscan
         ln -s %(prefix)s/opt/pfamscan/pfam_scan.pl %(prefix)s/bin"""
  #edef
