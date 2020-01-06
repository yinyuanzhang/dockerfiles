FROM docker.repository.cloudera.com/cdsw/engine:6
RUN echo "cdsw    ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN wget https://downloads.cloudera.com/connectors/impala_odbc_2.6.0.1000/Debian/clouderaimpalaodbc_2.6.0.1000-2_amd64.deb
RUN apt install -y ./clouderaimpalaodbc_2.6.0.1000-2_amd64.deb
RUN apt-get update
#RUN apt-get install -y libatlas-base-dev python-dev gfortran pkg-config libfreetype6-dev sudo
RUN apt-get install -y libffi-dev liblzma-dev gcc-4.9 g++-4.9 zlib1g-dev libncurses5-dev 
RUN apt-get install -y python3-all-dev libhdf5-dev libatlas-base-dev libopenblas-base libopenblas-dev libbz2-dev glpk-utils glpk-doc libglpk-dev glpk-utils python-glpk
