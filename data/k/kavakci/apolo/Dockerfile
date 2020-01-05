FROM node:lts-slim
RUN apt-get update \
    && apt-get install --no-install-recommends zip git  python-setuptools python python-pip curl -y \
    && apt-get clean --dry-run \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pytz \
    && pip install --no-cache-dir awsebcli \
    && pip install --no-cache-dir awscli\
    && eb --version \
    && aws --version \
    && node --version \
    && npm install -g @angular/cli \
    && aws configure set preview.cloudfront true
CMD ["/bin/bash"]
