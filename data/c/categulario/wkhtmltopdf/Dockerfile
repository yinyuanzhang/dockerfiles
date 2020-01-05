FROM buildpack-deps:stretch-curl

RUN apt-get update -y
RUN apt-get install -y \
    xz-utils \
    poppler-utils \
    gettext \
    libsasl2-dev \
    libssl1.0-dev \
    build-essential \
    libxrender1 \
    liblocale-msgfmt-perl
RUN curl -o wkhtmltox.tar.xz -SL https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
RUN echo '3f923f425d345940089e44c1466f6408b9619562 wkhtmltox.tar.xz' | sha1sum -c -
RUN tar xvf wkhtmltox.tar.xz
RUN cp wkhtmltox/lib/* /usr/local/lib/
RUN cp wkhtmltox/bin/* /usr/local/bin/
RUN rm wkhtmltox.tar.xz

CMD ["bash"]
