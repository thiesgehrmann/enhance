from package import *

class bioperl(Package):
    dependencies = ["expat",'perl','berkeleydb']
    def fetch(self):
      runCommand(self.fillVars("git clone https://github.com/bioperl/bioperl-live.git"))
    unpack = ""
    workdir = "bioperl-live"

    config = """
            PERL_MM_USE_DEFAULT=1 cpan Bundle::CPAN
            PERL_MM_USE_DEFAULT=1 cpan Module::Build
            PERL_MM_USE_DEFAULT=1 cpan DB_File
            (echo y;echo o conf prefer_installer MB;echo o conf commit)|cpan
            """

    build = """
            PERL_MM_USE_DEFAULT=1 perl ./Build.PL
            PERL_MM_USE_DEFAULT=1 ./Build 
           """

    install= """
            PERL_MM_USE_DEFAULT=1 ./Build install
            """

