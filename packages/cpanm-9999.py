from package import *

class cpanm(Package):
    dependencies = ['perl']

    def fetch(self):
      pass
    unpack = ""
    config = ""
    build = ""
    install="""cpan App::cpanminus"""
