FROM oaksharks/ubuntu-china-python36-jdk8:16.04
USER root
RUN pip3 install pypandoc
COPY requirements.txt /tmp
RUN pip3 install -i https://pypi.doubanio.com/simple --trusted-host pypi.doubanio.com --no-cache-dir -r "/tmp/requirements.txt"
# docker build -t oaksharks/py3-ml:16.04 .
