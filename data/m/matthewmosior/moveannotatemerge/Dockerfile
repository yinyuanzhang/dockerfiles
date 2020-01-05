#Work from the latest Haskell image.
FROM haskell:8

#Update apt-get and get vim.
RUN apt-get update -y && \
apt-get install -y vim && \
apt-get install -y libnss-sss && \
apt-get install -y libc6 && \
apt-get install -y git-core && \
apt-get install -y sudo 

#Make a new user (haskelluser).
RUN useradd -ms /bin/bash haskelluser

#Create a new group.
RUN addgroup --gid 1024 haskellgroup

#Give newgroup access to haskelluser.
RUN usermod -a -G haskellgroup haskelluser

#Add haskelluser to sudo group.
RUN chpasswd && adduser haskelluser sudo

#Set no password condition for sudo.
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

#Change working directory to /home/haskelluser.
WORKDIR "/home/haskelluser"

#Git clone the repository to /home/haskelluser.
RUN git clone https://github.com/Matthew-Mosior/Move-Annotate-Merge.git

#Change permissions of bin directory.
RUN chmod -R 777 /home/haskelluser/Move-Annotate-Merge

#Add symlink of bvf to bin.
RUN sudo ln -s /home/haskelluser/Move-Annotate-Merge/bin /bin

#Add stuff to path.
RUN export PATH="/opt/ghc/8.6.3/bin/:/usr/local/bin:/usr/bin:/opt/cabal/2.4/bin:/bin"

#Set the home directory.
ENV HOME=/home/haskelluser
