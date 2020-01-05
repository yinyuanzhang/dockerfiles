FROM cypress/browsers:node12.6.0-chrome75

RUN sed -i -r -e 's|deb(-src)? http://security.debian.org jessie/updates main||g' /etc/apt/sources.list \
    && echo "deb http://ftp.de.debian.org/debian testing main" >> /etc/apt/sources.list \
    && apt-get update && apt-get install -y --no-install-recommends \
         libc6-dev \
         python3.7 \
         python3.7-dev \
         python3-pip \
         python3-setuptools \
         python3-wheel \
    && rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python3 python /usr/bin/python3.7 100 && python3 --version

RUN pip3 install awscli nose pipenv==2018.10.13 requests

ENV PIPELINES_HELPER .bitbucket-pipelines/bitbucket-pipelines-helper.py

CMD ["/bin/sh"]
