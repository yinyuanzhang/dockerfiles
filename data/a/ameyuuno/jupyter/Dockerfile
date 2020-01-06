FROM ameyuuno/jupyter:base

LABEL maintainer="@ameyuuno <ameyuuno@gmail.com>"

USER root

COPY ./scripts/generate_jupyter_start_up_command.py /usr/bin/generate_jupyter_start_up_command.py
COPY ./scripts/start-jupyter.sh /usr/bin/start-jupyter.sh

ENV \
    JUPYTER_MODE=notebook \
    JUPYTER_HOST=0.0.0.0 \
    JUPYTER_PORT=8080 \
    JUPYTER_PASSWORD="" \
    JUPYTER_BASE_URL="/" \
    JUPYTER_WORKSPACE=${WORKSPACE_DIRECTORY} \
    SHELL=/bin/zsh

RUN \
    add-apt-repository -y ppa:jonathonf/python-3.6 && \
    apt-get update && \
    apt-get install -yq --no-install-recommends \
        fonts-liberation \
        inkscape \
        jed \
        libav-tools \
        libsm6 \
        libxext-dev \
        libxrender1 \
        lmodern \
        python3-dev \
        python3-setuptools \
        python3-wheel \
        python3-pip \
        python3.6 \
        python3.6-dev \
        texlive-fonts-extra \
        texlive-fonts-recommended \
        texlive-generic-recommended \
        texlive-latex-base \
        texlive-latex-extra \
        texlive-xetex && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    curl https://bootstrap.pypa.io/get-pip.py | python3.6 && \
    pip3.6 install --no-cache-dir \
        bokeh==0.13.0 \
        bpython==0.17.1 \
        cython==0.28.5 \
        ipykernel==5.1.0 \
        ipywidgets==7.4.2 \
        jupyterlab==0.34.12 \
        matplotlib==3.0.0 \
        notebook==5.7.0 \
        numpy==1.15.2 \
        pandas==0.23.4 \
        scikit-learn==0.20.0 \
        scipy==1.1.0 \
        seaborn==0.9.0 \
        tqdm==4.26.0 \
        virtualenv==16.2.0 \
        widgetsnbextension==3.4.2 && \
    chmod +x /usr/bin/generate_jupyter_start_up_command.py && \
    chmod +x /usr/bin/start-jupyter.sh 

CMD ["start-jupyter.sh"]

USER ${JD_USER}

RUN \
    echo "\nalias python=python3.6\nalias pip=pip3.6\n" >> ~/.zshrc && \
    virtualenv -p /usr/bin/python3.6 ~/.venv/ && \
    echo "\nsource ~/.venv/bin/activate\n" >> ~/.zshrc