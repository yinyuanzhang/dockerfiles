FROM ubuntu:18.04
MAINTAINER shishito.megane <shishito.megane3060.3@gmail.com>

# apt update
RUN apt-get update --fix-missing

# set language
RUN apt-get install -y language-pack-ja
ENV LANG=ja_JP.UTF-8 LC_ALL=ja_JP.UTF-8

# install packages
RUN apt-get install -y wget bzip2 ca-certificates curl git mariadb-client nano python3-dev sudo
RUN apt-get install -y build-essential libpq-dev
RUN apt-get install -y libgtk2.0-0 libgtk2.0-dev
RUN apt-get install -y libgl1-mesa-glx
RUN apt-get install -y lynx
RUN apt-get clean

# add sudo user
RUN groupadd -g 1000 developer && \
    useradd  -g      developer -G sudo -m -s /bin/bash self-position-estimation && \
    echo 'self-position-estimation:6RCxnLEG#/#!' | chpasswd

RUN echo 'Defaults visiblepw'             >> /etc/sudoers
RUN echo 'self-position-estimation ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# switch user
USER self-position-estimation
WORKDIR /home/self-position-estimation/

# install anaconda
ENV PATH /opt/conda/bin$PATH

RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.4.10-Linux-x86_64.sh -O /home/self-position-estimation/miniconda.sh && \
    /bin/bash /home/self-position-estimation/miniconda.sh -b -p /home/self-position-estimation/miniconda && \
    rm /home/self-position-estimation/miniconda.sh
ENV PATH /home/self-position-estimation/miniconda/bin:$PATH
RUN echo ". /home/self-position-estimation/miniconda/etc/profile.d/conda.sh" >> ~/.bashrc

# make working dir
RUN mkdir ./tmp/

# copy anaconda env file
COPY environment_ubuntu.yml ./tmp/

# import conda env & set
# RUN conda update -n base conda
RUN conda clean --all
RUN conda update --all
RUN conda update -n base conda
RUN conda env create -f ./tmp/environment_ubuntu.yml
RUN echo "conda activate flow-ubuntu" >> ~/.bashrc

# clean tmp file
RUN rm -rf ./tmp

# make app folder
RUN mkdir ./app

VOLUME ./app

CMD ["/bin/bash"]
