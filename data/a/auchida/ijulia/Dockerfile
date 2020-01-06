FROM julia:0.4
MAINTAINER Akihiro Uchida <uchida@turbare.net>

RUN apt-get update\
 && apt-get install -y curl bzip2\
 && apt-get install -y libglib2.0-0 libxext6 libsm6 libxrender1\
 && apt-get clean
RUN curl -sO https://repo.continuum.io/miniconda/Miniconda3-4.1.11-Linux-x86_64.sh\
 && /bin/bash Miniconda3-4.1.11-Linux-x86_64.sh -b -f -p /opt/miniconda\
 && /opt/miniconda/bin/conda install jupyter\
 && rm Miniconda3-4.1.11-Linux-x86_64.sh
ENV PATH /opt/miniconda/bin:$PATH
ENV LD_LIBRARY_PATH /opt/miniconda/lib:$LD_LIBRARY_PATH
RUN julia -e 'Pkg.add("IJulia")' && mkdir -p /data
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--notebook-dir=/data"]
