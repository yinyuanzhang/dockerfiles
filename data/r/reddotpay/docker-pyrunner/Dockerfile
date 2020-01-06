FROM reddotpay/docker-alpine-java:8u181b13_jdk-dcevm

COPY . /rdp-pyspark
WORKDIR /rdp-pyspark

ENV PYTHON_VERSION 2.7.15-r2
ENV PYSPARK_VERSION 2.2.1

ENV PIP get-pip.py
ADD https://bootstrap.pypa.io/get-pip.py /tmp/

ENV PYGLUE PyGlue.zip
ADD https://s3.amazonaws.com/aws-glue-jes-prod-us-east-1-assets/etl/python/PyGlue.zip /tmp/

RUN echo export PATH=${PATH}:~/.local/bin >> /etc/profile
RUN apk add --update --no-cache \
    curl \
    make \
    zip \
    python=$PYTHON_VERSION \
    python-dev \
    jq \
    gcc \
    g++ \
    bash \
    && rm -rf /var/cache/apk/*

RUN cd /tmp/ && python /tmp/${PIP}
RUN pip install awscli setuptools==4.0.1  \
    numpy==1.16.4 \
    autopep8==1.4.4 \
    virtualenv \
    pylint==1.9.5 \
    coverage \
    sphinx==1.8.5 \
    sphinx-rtd-theme==0.4.3 \
    boto3==1.9.199 \
    py4j==0.10.4 \
    s3pypi \
    pyspark==${PYSPARK_VERSION}
RUN pip install pandas==0.23.4

RUN cd /opt/ && unzip /tmp/${PYGLUE} && cp -R awsglue /usr/lib/python2.7/site-packages/awsglue
RUN rm -rf /tmp
