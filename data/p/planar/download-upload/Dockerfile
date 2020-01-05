FROM debian:stable
MAINTAINER Aleksey Yaroslavcev <a.yaroslavcev@gmail.com>

#Îáíîâëåíèå ñïèñêà è óñòàíîâêà ïàêåòîâ
RUN apt-get update;apt-get -y install wget curl git file lsb rsync tree

#Óñòàíîâêà è íàñòðîéêà LFS
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash;
RUN apt-get -y install git-lfs;git lfs install

#Î÷èñòêà êýøà ñêà÷åííûõ ïàêåòîâ
RUN apt-get -y clean;apt-get -y autoclean