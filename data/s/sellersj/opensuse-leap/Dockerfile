FROM opensuse/leap

RUN zypper --non-interactive install which curl wget \
    gcc curl-devel make autoconf gettext-devel openssl-devel zlib-devel perl-ExtUtils-MakeMaker \
    glibc glibc-devel vim glib2-devel-static glibc-devel-static libzstd-devel-static zlib-devel-static git
RUN zypper --non-interactive source-install git
