FROM centos:7

COPY bashrc /root/.bashrc
COPY texlive.profile /root

ENV TERM=xterm

RUN yum install -y which rsync perl-Tk perl-Digest-MD5 \
 wget gcc-c++ libSM libXext libXpm \
 && rsync --progress -v -a --delete rsync://mirrors.standaloneinstaller.com/ctan/systems/texlive/tlnet texlive \
 && cd texlive/tlnet && perl install-tl --profile /root/texlive.profile \
 && rm -rf /textlive \
 && cd \
 && wget https://root.cern.ch/download/root_v6.08.00.Linux-centos7-x86_64-gcc4.8.tar.gz \
 && tar -zvxf root_v6.08.00.Linux-centos7-x86_64-gcc4.8.tar.gz \
 && rm root_v6.08.00.Linux-centos7-x86_64-gcc4.8.tar.gz

