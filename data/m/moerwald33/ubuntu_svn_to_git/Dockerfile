FROM ubuntu:latest

# Add PPA to apt repository to fetch latest neovim version  -> see https://github.com/neovim/neovim/wiki/Installing-Neovim
RUN apt-get update \
 && apt-get -y install vim \
 && apt-get -y install subversion \
 && apt-get -y install git \
 && apt-get -y install git-svn 
 
RUN mkdir /data
CMD ["/bin/bash"]
