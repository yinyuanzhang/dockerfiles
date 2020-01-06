FROM ubuntu:16.04

WORKDIR /root

ENV SCALA_VERSION 2.12.8
ENV ALMOND_VERSION 0.2.1

COPY . /root

RUN apt-get update && \
    apt-get install -y \
    openjdk-8-jdk \
    python3 \
    python3-pip \
    curl

RUN pip3 install jupyter --ignore-installed

RUN curl -L -o coursier https://git.io/coursier && \
    chmod +x coursier && \
    ./coursier bootstrap -r jitpack \
    -i user -I user:sh.almond:scala-kernel-api_$SCALA_VERSION:$ALMOND_VERSION \
    sh.almond:scala-kernel_$SCALA_VERSION:$ALMOND_VERSION \
    --sources --default=true \
    -o almond && \
    ./almond --install && \
    rm coursier && \
    rm almond

RUN mkdir -p ~/.jupyter/custom && \
    cp ~/source/custom.js ~/.jupyter/custom/custom.js && \
    echo "import os\n\
from IPython.lib import passwd\n\
\n\
if 'PASSWORD' in os.environ:\n\
    password = os.environ['PASSWORD']\n\
    if password:\n\
        c.NotebookApp.password = passwd(password)\n\
    else:\n\
        c.NotebookApp.password = ''\n\
        c.NotebookApp.token = ''\n\
    del os.environ['PASSWORD']\n" >> ~/.jupyter/jupyter_notebook_config.py

EXPOSE 8888

ENTRYPOINT ["jupyter-notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
