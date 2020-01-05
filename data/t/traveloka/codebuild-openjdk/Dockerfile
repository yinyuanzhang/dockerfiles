FROM openjdk:8-slim
ADD https://raw.githubusercontent.com/traveloka/aws-sudo/master/aws-sudo.sh https://github.com/haya14busa/reviewdog/releases/download/0.9.11/reviewdog_linux_amd64 https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 beiscac_build beiscac_post_build /usr/local/bin/
ADD .beisca_reviewdog_default_all_errors.yml .beisca_reviewdog_default_all_warnings.yml /root/

RUN chmod 755 /usr/local/bin/*
RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl \
    python-pip \
    python-setuptools \
    python-wheel \
    && rm -rf /var/lib/apt/lists/*
RUN pip install awscli
