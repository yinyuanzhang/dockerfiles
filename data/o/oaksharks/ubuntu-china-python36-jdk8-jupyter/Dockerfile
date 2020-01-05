FROM oaksharks/py3-ml:latest
USER root
RUN pip3 install -i https://pypi.doubanio.com/simple --trusted-host pypi.doubanio.com --no-cache-dir -r "/tmp/requirements.txt"
COPY entrypoint.sh /
RUN mkdir /root/.jupyter && mkdir /opt/jupyter
COPY jupyter_notebook_config.py /root/.jupyter
RUN chmod +x /entrypoint.sh
ENV PYSPARK_PYTHON python3
EXPOSE 8888
CMD ["/bin/bash", "/entrypoint.sh"]
# docker build -t oaksharks/ubuntu-china-python36-jdk8-jupyter:16.04 .
