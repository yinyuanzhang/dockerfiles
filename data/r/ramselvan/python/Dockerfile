FROM ramselvan/neovim

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> /home/anbu/.zshrc && \
    echo "echo 'To activate anaconda type => conda activate base'" >> /home/anbu/.zshrc

RUN bash -c "/opt/conda/bin/conda install jupyter -y --quiet"

COPY setup_zsh.sh /
RUN apt-get -y purge python && apt-get -y autoremove
RUN bash -c "/setup_zsh.sh"
RUN bash -c "pip3 install pipenv"
RUN bash -c "rm -f /setup*.sh"

