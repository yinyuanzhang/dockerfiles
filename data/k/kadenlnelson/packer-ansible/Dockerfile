FROM hashicorp/packer:1.3.5

# update packages
RUN apk update

# install packages
RUN apk add --no-cache --update \
        python \
        python-dev \
        py-pip \
        build-base \
        libffi-dev \
        openssl-dev

# install ansible
RUN pip install ansible==2.7.9
