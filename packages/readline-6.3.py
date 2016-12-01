from package import *

class readline(MakePackage):
    dependencies = ["ncurses"]
    fetch="ftp://ftp.gnu.org/gnu/readline/readline-%(version)s.tar.gz"

    

