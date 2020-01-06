FROM centos:6
MAINTAINER Vladimir Kikhtenko <kikht@ict.nsc.ru>

WORKDIR /tmp/minit
RUN yum update -y && \
    yum install -y gcc make git && \
    git clone https://github.com/chazomaticus/minit.git . && \
    make && \
    make install && \
    rm -rf /tmp/minit && \
    yum remove -y \ 
        cloog-ppl            \ 
        cpp                  \ 
        fipscheck            \ 
        fipscheck-lib        \ 
        gcc                  \ 
        git                  \ 
        glibc-devel          \ 
        glibc-headers        \ 
        kernel-headers       \ 
        libedit              \ 
        libgomp              \ 
        mpfr                 \ 
        openssh              \ 
        openssh-clients      \ 
        perl                 \ 
        perl-Error           \ 
        perl-Git             \ 
        perl-Module-Pluggable\ 
        perl-Pod-Escapes     \ 
        perl-Pod-Simple      \ 
        perl-libs            \ 
        perl-version         \ 
        ppl                  \ 
        rsync               && \ 
    yum clean all
WORKDIR /

CMD ["minit"]
