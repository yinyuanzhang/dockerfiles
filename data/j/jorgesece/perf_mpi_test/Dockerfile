FROM ubuntu:16.04

ENV LD_LIBRARY_PATH=/liboverride:$LD_LIBRARY_PATH:/libfallback
ENV LD_RUN_PATH=/liboverride:$LD_RUN_PATH:/libfallback
ENV ctnlicense=/LICENSE
ENV PATH=/usr/bin:$PATH
ENV LD_LIBRARY_PATH=/usr/lib:$LD_LIBRARY_PATH
ENV LD_RUN_PATH=/usr/lib:$LD_RUN_PATH
ENV PATH=/app/openmpi/bin:$PATH
ENV LD_LIBRARY_PATH=/app/openmpi/lib:$LD_LIBRARY_PATH
ENV LD_RUN_PATH=/app/openmpi/lib:$LD_RUN_PATH

COPY run_test.sh /run_test.sh
COPY mpi_test_app.c /mpi_test_app.c

# post:
RUN sed -i /.singularity.d/actions/exec -e "s@^#\!\/bin/.*\$@#\!/bin/bash@" || echo '/.singularity.d/actions/exec not found.' && \
    sed -i /.singularity.d/actions/run -e "s@^#\!\/bin/.*\$@#\!/bin/bash@" || echo '/.singularity.d/actions/run not found.' && \
    sed -i /.singularity.d/actions/test -e "s@^#\!\/bin/.*\$@#\!/bin/bash@" || echo '/.singularity.d/actions/test not found.' && \
    sed -i /.singularity.d/runscript -e "s@^#\!\/bin/.*\$@#\!/bin/bash@" || echo '/.singularity.d/runscript not found.' && \
    sed -i /.singularity.d/test -e "s@^#\!\/bin/.*\$@#\!/bin/bash@" || echo '/.singularity.d/test not found.' && \
    sed -i /.exec -e "s@^#\!\/bin/.*\$@#\!/bin/bash@" || echo '/.exec not found.' && \
    sed -i /.run -e "s@^#\!\/bin/.*\$@#\!/bin/bash@" || echo '/.run not found.' && \
    sed -i /.test -e "s@^#\!\/bin/.*\$@#\!/bin/bash@" || echo '/.test not found.'

RUN chmod 755 /run_test.sh && \
    mkdir -p /app /liboverride /libfallback /prj /localscratch /localflash /opt $ctnlicense /scratch && \
    cd `mktemp -d --suffix=.bootstrap` || echo "/tmp not available" && \
    echo '[ -x $I_MPI_ROOT/intel64/bin/mpivars.sh ] && . $I_MPI_ROOT/intel64/bin/mpivars.sh' >> /environment && \
    grep universe /etc/apt/sources.list || sed -i 's/ main$/ main universe/' /etc/apt/sources.list && \
    apt-get -y update && \
    apt-get clean && \
    apt-get -y install gcc g++ gfortran     && \
    apt-get clean && \
    apt-get -y install make && \
    apt-get -y install cmake && \
    apt-get -y install autoconf && \
    apt-get -y install git && \
    apt-get -y install vim && \
    apt-get -y install curl hostname  && \
    apt-get -y install wget && \
    apt-get -y install unzip && \
    apt-get -y install tar && \
    apt-get -y install gzip && \
    apt-get -y install bc && \
    apt-get -y install less && \
    apt-get -y install util-linux && \
    apt-get -y install strace && \
    apt-get install -y bzip2 && \
    apt-get install -y man-db && \
    apt-get clean && \
    apt-get -y install cpuid && \
    apt-get -y install flex bison libbison-dev libfl-dev && \
    apt-get -y install binutils-dev libnuma-dev libunwind-dev && \
    apt-get -y install libelf-dev libelf1 && \
    apt-get -y install systemtap-sdt-dev libaudit1 libaudit-dev && \
    apt-get -y install libssl-dev libssl1.0.0 libslang2-dev libslang2 && \
    apt-get -y install libperl-dev  && \
    apt-get -y install liblzma-dev xz-utils && \
    apt-get -y install numactl libnuma-dev  && \
    apt-get -y install elfutils libdw-dev && \
    apt-get -y install libunwind-dev && \
    apt-get -y install binutils-dev binutils libiberty-dev && \
    apt-get -y install libpython2.7-dev python-dev libpython-dev && \
    apt-get -y install e2fslibs e2fslibs-dev e2fsprogs && \
    #apt-get -y install linux-tools-`uname -r` && \
    #apt-get -y install linux-cloud-tools-`uname -r` && \
    apt-get -y install libtool libtool-bin autopoint gettext && \
    apt-get -y install pkg-config autoconf libncurses5-dev && \
    apt-get clean && \
    echo '2ca34f40067b0c914dbe474bd4ce44dbaec068d684d870c93953480062ce0e42ae32d70392ed572b1cf683ef06683f73c9d98e883405fb75ccbf614a732ce009  -' > dstat.zip.sha512 && \
    curl -sSL "https://github.com/dagwieers/dstat/archive/0.7.3.zip" | tee dstat.zip | sha512sum -c dstat.zip.sha512 && \
    unzip -q dstat.zip && rm -f dstat.zip* && \
    cat dstat-*/COPYING > $ctnlicense/dstat.COPYING && \
    cd dstat-* && \
    make install && \
    cd -  && \
    rm -rf dstat-* && \
    echo '5aee3e0b77ff9895ee7e214552c14124f90defa72f15811db81a89e7e09c66ee643a3d1c90a97358b049c863ebe8a811355d758729ca6012bc52e822e54cc044  -' > perf.zip.sha512 && \
    curl -sSL "https://github.com/torvalds/linux/archive/v4.10.zip" | tee perf.zip | sha512sum -c perf.zip.sha512 && \
    unzip -q perf.zip && rm -f perf.zip* && \
    cat linux-*/COPYING > $ctnlicense/perf.COPYING && \
    cd linux-*/tools/perf && \
    make CFLAGS=-static LDFLAGS=-static && \
    strip perf && \
    mv perf /usr/bin/ && \
    cd - && \
    rm -rf linux-* && \
    echo '985354a62702d3d75adfe59cf78e73651a9c893806970ee46eb26693a4c82ca2efdd1d0e871a9c56bbc14a8b44f76eca5b2cd8e45da696a20fa588bb45533e11  -' > flock.zip.sha512 && \
    curl -sSL 'https://github.com/karelzak/util-linux/archive/v2.23.2.zip' | tee flock.zip | sha512sum -c flock.zip.sha512 && \
    unzip -q flock.zip && rm -f flock.zip* && \
    cd util-linux-* && \
    ./autogen.sh && \
    ./configure --disable-silent-rules && \
    make flock && rm -f flock && \
    gcc -static -std=gnu99 -fsigned-char -fno-common -Wall -Werror=sequence-point -Wextra -Wmissing-declarations -Wmissing-parameter-type -Wmissing-prototypes -Wno-missing-field-initializers -Wredundant-decls -Wsign-compare -Wtype-limits -Wuninitialized -Wunused-but-set-parameter -Wunused-but-set-variable -Wunused-parameter -Wunused-result -Wunused-variable -Wnested-externs -Wpointer-arith -Wstrict-prototypes -g -O2 -o flock sys-utils/flock.o  ./.libs/libcommon.a && \
    strip flock && \
    mv flock /usr/bin/ && \
    cd - && \
    rm -rf util-linux-* && \
    echo '600a0161d7eca085594191b133cb25ec6bb6db41d0857cfac7f6b3bdf45647961f329c4cd423fd3dacb34fd09183b762c0b70bcd7b06a878666c8a241c3a7e53  -' > pmu-tools.zip.sha512 && \
    curl -sSL "https://github.com/andikleen/pmu-tools/archive/r105.zip" | tee pmu-tools.zip | sha512sum -c pmu-tools.zip.sha512 && \
    unzip -q pmu-tools.zip -d /app && rm -rf pmu-tools.zip* && \
    cat /app/pmu-tools*/COPYING > $ctnlicense/pmu-tools.COPYING && \
    echo '904b77f97bdb029f9262f8816b2ccd6a16d986702682874196a7d68683b9749916554fc81ad76c83a05e5211b417aa3694cd955e2cb31ec3c421947331cc8f7a  -' > likwid.zip.sha512 && \
    curl -sSL "https://github.com/RRZE-HPC/likwid/archive/likwid-4.2.zip" | tee likwid.zip|sha512sum -c likwid.zip.sha512 && \
    unzip -q likwid.zip && rm -f likwid.zip* && \
    cd likwid-* && \
    cat COPYING > $ctnlicense/likwid.COPYING && \
    make && \
    make install && \
    cd - && \
    rm -rf likwid-* && \
    echo 'b0ede0264cd9263b8ba59ec51d17ad47b5f20d49d219ca05f7c396d608398d517b2023a46a2535fd6191160d709e4805c4de436dcfee56eda287383bd69f9652  -' > openmpi.tar.bz2.sha512     && \
    curl -sSL "https://www.open-mpi.org/software/ompi/v1.6/downloads/openmpi-1.6.5.tar.bz2" | tee openmpi.tar.bz2 | sha512sum -c openmpi.tar.bz2.sha512 && \
    tar -jxf openmpi.tar.bz2 && rm -f openmpi.tar.bz2* && \
    cd openmpi-* && \
    cat LICENSE > $ctnlicense/OpenMPI.LICENSE && \
    ./configure --prefix=/app/openmpi --with-verbs && \
    make && \
    make install && \
    cd - && \
    rm -rf openmpi-*

RUN    mpicc -Wall /mpi_test_app.c -o mpi_test_app && chmod +x mpi_test_app && mv mpi_test_app /app/mpi_test_app && echo "/app/mpi_test_app || rm my_output_iotest.bin" > /run_test.sh &&  chmod +x /run_test.sh
