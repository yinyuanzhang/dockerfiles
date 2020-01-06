FROM amazonlinux:2018.03

# Grab requirements.txt.
ADD requirements.txt /tmp/requirements.txt

RUN yum update; \
    yum install -y \
      python36 \
      libgomp && \
      curl -O https://bootstrap.pypa.io/get-pip.py && \
      python3.6 get-pip.py && \
      rm get-pip.py && \
      pip3 install -qr /tmp/requirements.txt && \
    yum clean all && rm -rf /tmp/* /var/tmp/*