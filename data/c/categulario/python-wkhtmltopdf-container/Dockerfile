FROM python:3.7.0-slim-stretch

RUN apt-get update -y && apt-get install -y \
    python3-dev \
    curl \
    xz-utils \
    poppler-utils \
    gettext \
    libsasl2-dev \
    libssl1.0-dev \
    build-essential \
    libxrender1 \
    liblocale-msgfmt-perl \
    default-libmysqlclient-dev \
    && curl -o wkhtmltox.tar.xz -SL https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
    && echo '3f923f425d345940089e44c1466f6408b9619562 wkhtmltox.tar.xz' | sha1sum -c - \
    && tar xvf wkhtmltox.tar.xz \
    && cp wkhtmltox/lib/* /usr/local/lib/ \
    && cp wkhtmltox/bin/* /usr/local/bin/ \
    && cp -r wkhtmltox/share/man/man1 /usr/local/share/man/
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

CMD ["bash"]
