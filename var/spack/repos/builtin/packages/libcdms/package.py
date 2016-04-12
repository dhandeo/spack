# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install libcdms
#
# You can always get back here to change things with:
#
#     spack edit libcdms
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class Libcdms(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/UV-CDAT/libcdms/archive/uvcdat-2.4.1.tar.gz"

    version('2.4.1', '3d6791723c86fbfb1ad43b1d099d86fd')
    version('2.4.0', '668fa70ba048f640f92182f8ec871174')

    # FIXME: Add dependencies if this package requires them.
    # depends_on("foo")

    def install(self, spec, prefix):
        # FIXME: Modify the configure line to suit your build system here.
        configure('--prefix=%s' % prefix)

        # FIXME: Add logic to build and install here
        make(parallel=False)
        make("install", parallel=False)
