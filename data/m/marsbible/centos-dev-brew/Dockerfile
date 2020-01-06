FROM centos:7

MAINTAINER kevin ma <redshift@outlook.com>

RUN yum -y update \
 && yum -y group install "Development Tools" \
 && localedef -c -f UTF-8 -i en_US en_US.UTF-8 \
 && yum -y install sudo openssl wget file unzip git vim curl \
 && yum -y clean all \
 && useradd --create-home --shell /bin/bash linuxbrew -G wheel \
 && echo "linuxbrew:linuxbrew" | chpasswd \
 && curl -fsSL https://patch-diff.githubusercontent.com/raw/boostorg/variant/pull/68.patch -o /home/linuxbrew/68.patch

USER linuxbrew 
WORKDIR /home/linuxbrew

# x86_64 only
ENV CFLAGS="-march=sandybridge"
ENV CXXFLAGS="-march=sandybridge"

ENV LC_ALL en_US.UTF-8
ENV HOMEBREW_NO_AUTO_UPDATE=1
ENV ACLOCAL_PATH /home/linuxbrew/.linuxbrew/share/aclocal
ENV CMAKE_INSTALL_PREFIX /home/linuxbrew/.linuxbrew
ENV CMAKE_PREFIX_PATH /home/linuxbrew/.linuxbrew
ENV CMAKE_INCLUDE_PATH /home/linuxbrew/.linuxbrew/include
ENV CMAKE_LIBRARY_PATH /home/linuxbrew/.linuxbrew/lib
ENV PKG_CONFIG_PATH /usr/local/lib/pkgconfig:/usr/local/lib64/pkgconfig:/usr/lib64/pkgconfig:/usr/lib/pkgconfig:/usr/lib/x86_64-linux-gnu/pkgconfig:/usr/lib64/pkgconfig:/usr/share/pkgconfig:$PKG_CONFIG_PATH
ENV LINUXBREWHOME /home/linuxbrew/.linuxbrew
ENV PATH $LINUXBREWHOME/bin:$PATH
ENV MANPATH $LINUXBREWHOME/man:$MANPATH
ENV PKG_CONFIG_PATH $LINUXBREWHOME/lib64/pkgconfig:$LINUXBREWHOME/lib/pkgconfig:$PKG_CONFIG_PATH


RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)" \
  && curl -fsSL https://raw.githubusercontent.com/marsbible/linuxbrew-core/fbthrift/Formula/gflags.rb -o /home/linuxbrew/.linuxbrew/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/gflags.rb \
  && curl -fsSL https://raw.githubusercontent.com/marsbible/linuxbrew-core/fbthrift/Formula/glog.rb -o /home/linuxbrew/.linuxbrew/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/glog.rb \  
  && curl -fsSL https://raw.githubusercontent.com/marsbible/linuxbrew-core/folly-fix/Formula/double-conversion.rb -o /home/linuxbrew/.linuxbrew/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/double-conversion.rb \
  && curl -fsSL https://raw.githubusercontent.com/marsbible/linuxbrew-core/folly-fix/Formula/folly.rb -o /home/linuxbrew/.linuxbrew/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/folly.rb \
  && brew install jemalloc \
  && brew install folly
