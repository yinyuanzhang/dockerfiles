FROM pyypl/raiden:latest

RUN apt-get -y update \
  && apt-get install -y python-pip \
  && rm -rf /var/lib/apt/lists/*

RUN pip install awscli

COPY entrypoint.sh /
COPY ssm-env.sh /
COPY raiden.sh /

ENTRYPOINT ["/entrypoint.sh"]
