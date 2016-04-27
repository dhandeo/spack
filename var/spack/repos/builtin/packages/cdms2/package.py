from spack import *

class Cdms2(Package):
    """Climate Model Output Rewriter"""

    homepage = "https://pcmdi.github.io/cmor-site"
    url      = "https://github.com/UV-CDAT/uvcdat/archive/v2.4.1.tar.gz"

    version('2.4.1', 'e54851295952891dabd0fe3840f59f3b')

    # depends_on('ossp-uuid')
    # depends_on('udunits2')
    # depends_on('python')

    extends('python')
    depends_on('py-pygments')
    depends_on('py-setuptools')

    def install(self, spec, prefix):
        with working_dir('Packages/cdms2'):
            python('setup.py', 'install', '--prefix=%s' % prefix)

    # def install(self, spec, prefix):
        # with working_dir('Packages/cdms2'):
            # configure("--prefix=%s" % prefix,
                      # "--with-python")
            # make()
            # make("install")
