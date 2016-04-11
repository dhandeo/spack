from spack import *

class Jasper(Package):
    """Description"""

    homepage = "http://www.ece.uvic.ca/~frodo/jasper/"
    url      = "http://www.ece.uvic.ca/~frodo/jasper/software/jasper-1.900.1.zip"

    version('1.900.1', 'a342b2b4495b3e1394e161eb5d85d754')

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix)
        make()
        make("install")
