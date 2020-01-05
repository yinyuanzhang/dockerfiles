FROM python:3.7.3-stretch

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
        apache2 \
        apache2-dev \
        curl \
        gnupg \
        libapache2-mod-shib2 \
        libapache2-mod-wsgi-py3 \
        libc-dev-bin \
        libc6-dev \
        libc6-dev-i386 \
        libc6-i386 \
        linux-libc-dev \
        python3-dev
RUN curl -sL https://deb.nodesource.com/setup_11.x  | bash - && \
    curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get -y update && apt-get -y install nodejs yarn && rm -rf /var/lib/apt/lists/*

COPY watchman /usr/local/bin/watchman

WORKDIR /usr/src/app

RUN pip install --no-cache-dir pipenv

CMD ["python"]
