from package import *

class git(Package):
    dependencies = ["python",'openssl','zlib','curl','perl']

    fetch="https://github.com/git/git/archive/master.zip"

    def unpack(self, infile, outfile):
      runCommand("pwd; ls")
      runCommand("unzip %s %s" % (infile, outfile))


    def install(self):
      install="cd git-master && make PYTHON_PATH=%(prefix)s/bin/python NO_EXPAT=YesPlease NO_TCLTK=YesPlease PERL_PATH=%(prefix)s/bin/perl prefix=%(prefix)s all install"
      runCommand(self.fillVars(install))

