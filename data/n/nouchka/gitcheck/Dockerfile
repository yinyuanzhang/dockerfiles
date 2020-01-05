FROM badele/alpine-python:2.7
MAINTAINER Bruno Adelé "bruno@adele.im"

# Install requirements installation
RUN apk add --update git && rm -rf /var/cache/apk/*

# Install gitcheck
RUN pip install git+git://github.com/yucer/gitcheck.git@fix_setup_py

# default command
CMD cd /files && gitcheck
