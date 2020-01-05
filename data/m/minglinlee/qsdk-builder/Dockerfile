FROM ubuntu:14.04
MAINTAINER minglin.le@gmail.com
LABEL description="QSDK Image Builder docker image" version="0.1"

ENV UID="1000" \
    GID="1000" \
    USER_NAME="autobuild" \
    USER_EMAIL="autobuild@email" \
    PROJECTBASEDIR="src" \
    PROJECTDIR="" \
    PROJECTJOBS="1" \
    MANIFEST_URL="git://codeaurora.org/quic/qsdk/releases/manifest/qstak" \
    MANIFEST_XML="default.xml" \
    MANIFEST_BRANCH="release" \
    GITREPO_HOST="" \
    GITREPO_BRANDH=""

RUN apt-get update &&\
    apt-get install -y sudo vim time git-core tig subversion build-essential gcc-multilib \
			libncurses5-dev zlib1g-dev gawk flex gettext wget unzip python python-yaml \
			binutils binutils-gold patch bzip2 make pkg-config libc6-dev \
			sharutils curl libxml-parser-perl libssl-dev libssl0.9.8\
			gcc-4.4 g++-4.4 gcc-4.4-multilib binutils ocaml-nox ocaml-nox ocaml ocaml-findlib \
			libpcre3-dev bsdmainutils u-boot-tools device-tree-compiler mtd-utils && \
    apt-get clean

RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.4 20 && \
	update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 10 && \
	update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.4 20 && \
	update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 10 && \
	update-alternatives --install /usr/bin/cc cc /usr/bin/gcc 20 && \
	update-alternatives --set cc /usr/bin/gcc && \
	update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++ 20 && \
	update-alternatives --set c++ /usr/bin/g++

COPY ["run.sh","git-repo/repo",".env","/"]

ENTRYPOINT ["/run.sh"]
CMD ["init","sync","update","build"]
