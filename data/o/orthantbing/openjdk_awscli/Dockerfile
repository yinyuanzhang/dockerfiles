FROM  openjdk:8-jdk

RUN apt-get --quiet update --yes && \
    apt-get --quiet install --yes \
        python3 \
        python3-pip \
        python3-setuptools \
        groff \
        less \
        jq \
        zip \
        wget \
        tar \
        unzip \
        lib32stdc++6 \ 
        lib32z1

RUN pip3 --no-cache-dir install --upgrade awscli

CMD ["/bin/bash"]