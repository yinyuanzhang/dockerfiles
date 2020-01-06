FROM tensorflow/tensorflow:latest-gpu

# update
RUN apt-get -y update
RUN apt-get -y upgrade

# install vim
RUN apt-get -y install vim

# clean
RUN  apt-get -y clean

CMD ["/run_jupyter.sh", "--allow-root"]
