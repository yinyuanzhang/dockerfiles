FROM ubuntu:latest

# Add PPA to apt repository to fetch latest neovim version  -> see https://github.com/neovim/neovim/wiki/Installing-Neovim
RUN apt-get update \
 && apt-get -y install software-properties-common 
 
RUN mkdir /data
CMD ["/bin/bash"]
