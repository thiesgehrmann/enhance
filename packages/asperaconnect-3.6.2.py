from package import *
import subprocess

class asperaconnect(MakePackage):

  fetch="http://download.asperasoft.com/download/sw/connect/3.6.2/aspera-connect-3.6.2.117442-linux-64.tar.gz"

  def unpack(self, infile, outfile):
    runCommand("tar -xvf %s %s" % (infile, outfile))
    return "./"
    
  workdir = ""

  config=""

  def build(self):
    tarball_name = self.fetch.split('/')[-1][:-7]
    skipcmd = "awk '/^__ARCHIVE_FOLLOWS__/ { print NR + 1; exit 0; }' %%(srcpath)s/%s.sh > skiplines.txt" % tarball_name
    skipcmd = self.fillVars(skipcmd)
    runCommand(skipcmd)
    runCommand("tail -n +`cat skiplines.txt` %s.sh | tar xzpo -C ./ -f -" % (tarball_name))

  def install(self):
    c="""pwd
         mkdir -p %(prefix)s/opt/asperaconnect/3.6.2/
         cp -r %(srcpath)s/bin %(prefix)s/opt/asperaconnect/3.6.2/
         cp -r %(srcpath)s/lib %(prefix)s/opt/asperaconnect/3.6.2/
         cp -r %(srcpath)s/etc %(prefix)s/opt/asperaconnect/3.6.2/
         ln -s %(prefix)s/opt/asperaconnect/3.6.2/bin/asperaconnect %(prefix)s/bin
         ln -s %(prefix)s/opt/asperaconnect/3.6.2/bin/ascp %(prefix)s/bin
    """;
    for cmd in c.split('\n'):
      runCommand(self.fillVars(cmd))

