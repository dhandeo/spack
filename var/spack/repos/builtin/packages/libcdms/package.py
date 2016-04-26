from spack import *


class Libcdms(Package):
    """Climate Data Management System Library """

    homepage = "https://github.com/UV-CDAT/libcdms"
    url      = "https://github.com/UV-CDAT/libcdms/archive/uvcdat-2.4.1.tar.gz"

    version('2.4.1', '3d6791723c86fbfb1ad43b1d099d86fd')
    version('2.4.0', '668fa70ba048f640f92182f8ec871174')

    # TODO: add optional packages
    depends_on("python")

    def install(self, spec, prefix):
        # TODO: add optional packages
        configure('--prefix=%s' % prefix)

        # Make directories at the destination as the build script does not
        mkdirp(prefix.bin)
        mkdirp(prefix.include)
        mkdirp(prefix.lib)

        # FIXME: Add logic to build and install here
        make(parallel=False)
        make("bininstall", parallel=False)
        make("libinstall", parallel=False)
