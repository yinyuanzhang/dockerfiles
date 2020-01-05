FROM debian:latest
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 git
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh -O ~/Anaconda3-2019.03-Linux-x86_64.sh && /bin/bash ~/Anaconda3-2019.03-Linux-x86_64.sh -b -p /opt/anaconda3 && rm ~/Anaconda3-2019.03-Linux-x86_64.sh
ENV PATH=/opt/anaconda3/bin:PATH
ENTRYPOINT ["/bin/sh"]