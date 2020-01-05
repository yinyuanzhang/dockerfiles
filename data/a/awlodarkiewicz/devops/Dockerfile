FROM awlodarkiewicz/devops:base

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-add-repository -y ppa:ansible/ansible && \
    apt-get update && \
    apt-get -qq -y --no-install-recommends install \
        aptitude software-properties-common \
        python bash ca-certificates ansible && \
    apt-get -y autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    ansible-galaxy install geerlingguy.docker
