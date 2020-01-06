FROM ubuntu:16.04
LABEL author=lozzow

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PATH=$PATH:/usr/local/go/bin \
    PKG_CONFIG_PATH=/usr/local/lib/pkgconfig \
    GOPATH=/root/go

RUN apt update --fix-missing \
    && apt install -y software-properties-common \
    && add-apt-repository ppa:jonathonf/python-3.6 \
    && apt update \
    && apt install -y libzmq3-dev git wget r-base libcurl4-openssl-dev libssl-dev libssl-dev pkg-config curl python3.6 python3.6-dev \
    && wget https://dl.google.com/go/go1.11.linux-amd64.tar.gz \
    && tar -C /usr/local -xzf go1.11.linux-amd64.tar.gz \
    && rm go1.11.linux-amd64.tar.gz \
    && apt remove -y software-properties-common \
    && apt autoremove -y \
    && curl -o /tmp/get-pip.py "https://bootstrap.pypa.io/get-pip.py" \
    && python3.6 /tmp/get-pip.py \
    && pip3 install jupyter \
    && (echo "install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest'),repos = 'https://mirrors.tuna.tsinghua.edu.cn/CRAN')" \
    && echo "devtools::install_github('IRkernel/IRkernel')"  \
    && echo "IRkernel::installspec()" ) | Rscript -e "source(file('stdin'))" \
    && go get -u github.com/gopherdata/gophernotes \
    && cp $GOPATH/bin/gophernotes /usr/local/bin/ \
    && mkdir -p ~/.local/share/jupyter/kernels/gophernotes \
    && cp -r $GOPATH/src/github.com/gopherdata/gophernotes/kernel/* ~/.local/share/jupyter/kernels/gophernotes \
    && rm -rf /var/lib/apt/lists/* \
    && apt clean \
    && jupyter notebook --generate-config


# ADD entrypoint.sh /entrypoint.sh

EXPOSE 8888

# ENTRYPOINT ["/entrypoint.sh"]

CMD ["jupyter", "notebook", "--no-browser", "--allow-root", "--ip=0.0.0.0"]
