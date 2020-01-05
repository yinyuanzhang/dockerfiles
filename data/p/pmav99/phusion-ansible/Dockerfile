FROM phusion/baseimage:0.11

# Install ansible
RUN apt update \
 && apt upgrade -y -o Dpkg::Options::="--force-confold" \
 && apt install -y \
        -o APT::Install-Recommends=false \
        -o APT::Install-Suggests=false \
        sudo \
        python3 \
        python3-pip \
 # install ansible via pip
 && pip3 install setuptools \
 && pip3 install ansible \
 && ln -s /usr/bin/python3 /usr/bin/python \
 # clean up
 && apt autoremove -y \
 && apt clean \
 && rm -rf /var/lib/apt/lists/* \
           /var/tmp/* \
           /usr/share/doc \
           /usr/share/man \
 # remove python files
 && rm -rf /root/.cache/pip/ \
 && find / -name '*.pyc' -delete \
 && find / -name '*__pycache__*' -delete
