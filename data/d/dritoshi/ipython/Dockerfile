FROM ubuntu:14.04
MAINTAINER Itoshi NIKAIDO "dritoshi@gmail.com"

RUN locale-gen en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8
ENV LC_ALL C
ENV LC_ALL en_US.UTF-8

# apt-get
ENV DEBIAN_FRONTEND noninteractive
RUN echo "deb http://jp.archive.ubuntu.com/ubuntu/ trusty main restricted\n\
deb-src http://jp.archive.ubuntu.com/ubuntu/ trusty main restricted\n\
deb http://jp.archive.ubuntu.com/ubuntu/ trusty-updates main restricted\n\
deb-src http://jp.archive.ubuntu.com/ubuntu/ trusty-updates main restricted\n\
deb http://jp.archive.ubuntu.com/ubuntu/ trusty universe\n\
deb-src http://jp.archive.ubuntu.com/ubuntu/ trusty universe\n\
deb http://jp.archive.ubuntu.com/ubuntu/ trusty-updates universe\n\
deb-src http://jp.archive.ubuntu.com/ubuntu/ trusty-updates universe\n\
deb http://jp.archive.ubuntu.com/ubuntu/ trusty multiverse\n\
deb-src http://jp.archive.ubuntu.com/ubuntu/ trusty multiverse\n\
deb http://jp.archive.ubuntu.com/ubuntu/ trusty-updates multiverse\n\
deb-src http://jp.archive.ubuntu.com/ubuntu/ trusty-updates multiverse\n\
deb http://jp.archive.ubuntu.com/ubuntu/ trusty-backports main restricted universe multiverse\n\
deb-src http://jp.archive.ubuntu.com/ubuntu/ trusty-backports main restricted universe multiverse\n\
deb http://security.ubuntu.com/ubuntu trusty-security main restricted\n\
deb-src http://security.ubuntu.com/ubuntu trusty-security main restricted\n\
deb http://security.ubuntu.com/ubuntu trusty-security universe\n\
deb-src http://security.ubuntu.com/ubuntu trusty-security universe\n\
deb http://security.ubuntu.com/ubuntu trusty-security multiverse\n\
deb-src http://security.ubuntu.com/ubuntu trusty-security multiverse\n"> /etc/apt/sources.list

# CRAN
RUN echo "deb http://cran.ism.ac.jp/bin/linux/ubuntu trusty/" >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9

RUN apt-get update
RUN apt-get upgrade -y

# `python3-pip` depends on `python3-devel`.
RUN apt-get install -y python3-pip libfreetype6-dev libxft-dev
RUN apt-get install -y gfortran libopenblas-dev liblapack-dev

# Exporting HTML requires either of Node.JS or Pandoc.
RUN apt-get install -y nodejs

# Use `pip` to make sure latest versions.
RUN pip3 install pyzmq
RUN pip3 install numpy
RUN pip3 install matplotlib
RUN pip3 install pandas
RUN pip3 install scipy
RUN pip3 install scikit-learn
RUN pip3 install networkx
RUN pip3 install Sphinx
RUN pip3 install ipython[notebook]

# R/Bioconductor
RUN apt-get install -y r-base r-base-dev wget

# SSH
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

# For IPython Notebook to share resources with host.
EXPOSE 8888
VOLUME ["/notebook"]
ADD ipython-notebook-startup.sh /usr/local/bin/ipython-notebook-startup.sh

CMD ["ipython-notebook-startup.sh" , "/notebook"]

RUN apt-get clean
