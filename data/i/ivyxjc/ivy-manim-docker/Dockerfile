FROM python:3.7
# RUN sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list
RUN apt-get update \
    && apt-get install -qqy --no-install-recommends \
        apt-utils \
        ffmpeg \
        sox \
        libcairo2-dev \
        texlive \
        texlive-fonts-extra \
        texlive-latex-extra \
        texlive-latex-recommended \
        texlive-science \
        tipa \
        python3-pip\
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install \
    # -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com  \
    argparse==1.4.0 \
    colour==0.1.5 \
    numpy==1.15.0 \
    Pillow==5.2.0 \
    progressbar==2.5 \
    scipy==1.1.0 \
    tqdm==4.24.0 \
    opencv-python==3.4.2.17 \
    pycairo==1.17.1 \
    pydub==0.23.0
ENTRYPOINT ["/bin/bash"]
