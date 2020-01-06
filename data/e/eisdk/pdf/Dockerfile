FROM ubuntu:16.04

RUN apt-get update && apt-get install -y -f software-properties-common \
    && apt-get update \
    && apt-get install -y -f python-pip build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install werkzeug executor gunicorn

COPY multiverse.list /etc/apt/sources.list.d


RUN  apt-get -qq update \
    && apt-get install -y -f  apt-transport-https xfonts-base xfonts-75dpi xserver-common libssl-dev libxrender-dev libjpeg8 fontconfig curl wget \
    && apt-get clean \
    && apt-get autoremove -y

# Accept EULA for MS fonts
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections # Accept EULA for MS fonts

RUN  apt-get -qq update \
    && apt-get install -y -f  ttf-mscorefonts-installer \
    && apt-get clean \
    && apt-get autoremove -y


COPY app.py /

# RUN wget https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
# RUN tar xf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz

RUN wget https://downloads.wkhtmltopdf.org/0.12/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz
RUN tar xf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz

RUN ln -s /wkhtmltox/bin/wkhtmltopdf /usr/local/bin/.


EXPOSE 80

ENTRYPOINT ["/usr/local/bin/gunicorn"]

CMD ["-b", "0.0.0.0:80", "--log-file", "-", "app:application"]

