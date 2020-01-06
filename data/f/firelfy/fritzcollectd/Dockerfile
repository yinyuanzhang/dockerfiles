FROM debian:stretch-slim

# install collectd
RUN apt-get update -y && apt-get install --no-install-recommends -y \
    collectd

# install fritzbox plugin
RUN apt-get install --no-install-recommends -y \
    libpython2.7 \
    python-setuptools \
    python-wheel \
    python-pip
RUN pip install fritzcollectd

CMD ["collectd", "-f"]
