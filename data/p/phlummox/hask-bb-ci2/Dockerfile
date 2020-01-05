FROM ubuntu:precise

RUN apt-get update

# the software-properties packages are needed for add-apt-repository
# r-base-dev has a good selection of ubuntu -dev libraries
RUN : "handy packages" && \
  apt-get install -y \
    curl        \
    git         \
    less        \
    mercurial   \
    python-software-properties \
    r-base-dev \
    software-properties-common \
    sudo \
    wget   

RUN : "useful build tools" && \
  apt-get install -y \ 
    alien             \
    binutils          \
    bsdmainutils      \
    build-essential   \
    coreutils         \
    cpio              \
    diffutils         \
    fakeroot          \
    file              \
    findutils         \
    gawk              \
    gnupg             \
    kernel-package    \
    less              \
    make              \
    netcat            \
    net-tools         \
    patchutils        \
    rsync             \
    sudo              \
    sudo              \
    tar               \
    vim-tiny                            


RUN : "haskell repos" && \
  add-apt-repository -y ppa:hvr/ghc && \
  apt-get update 

RUN : "haskell tools" && \
 apt-get install -y \
  alex-3.1.7 \
  cabal-install-1.18 \
  cabal-install-1.24 \
  ghc-7.10.3 \
  ghc-8.0.1 \
  happy-1.19.5

RUN : "non-root user" && \
  addgroup --gid 1024 user && \
  adduser --home /home/user --disabled-password --shell /bin/bash --gid 1024 --uid 1024 --gecos '' user && \
  echo '%user ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER user

ENV PATH /home/user/.cabal/bin:/home/user/.local/bin:/opt/cabal/1.24/bin:/opt/ghc/8.0.1/bin:/opt/happy/1.19.5/bin:/opt/alex/3.1.7/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN : "init cabal, install stack" && \
  cabal update && \
  (echo 'jobs: $ncpus' >> $HOME/.cabal/config) && \
  mkdir -p ~/.local/bin && \
  curl -L https://www.stackage.org/stack/linux-x86_64 | tar xz --wildcards --strip-components=1 -C ~/.local/bin '*/stack' && \
  stack setup

RUN : "setup stack lts-6 and lts-7" && \
  stack setup --resolver lts-6 && \
  stack setup --resolver lts-7 


#WORKDIR /home

CMD ["bash"]



