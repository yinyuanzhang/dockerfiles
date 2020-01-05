# Docker image for developing kwant
FROM kwant/testing

MAINTAINER Kwant developers <authors@kwant-project.org>


# Install Tini
RUN apt-get update && apt-get install -y wget
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.10.0/tini && \
    echo "1361527f39190a7338a0b434bd8c88ff7233ce7b9a4876f3315c22fce7eca1b0 *tini" | sha256sum -c - && \
    mv tini /usr/local/bin/tini && \
    chmod +x /usr/local/bin/tini


# setup jupyter notebook
RUN pip3 install \
    notebook==5.0.0 \
    sympy==1.0


# add /opt/bin to the PATH
ENV PATH="/opt/bin:${PATH}"


# create user used by start.sh
ENV NB_USER developer
ENV NB_UID 1000
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER
RUN mkdir /notebooks /kwant && chown -R $NB_UID:users /notebooks /kwant


# Configure container startup
VOLUME /notebooks /kwant
WORKDIR /notebooks
EXPOSE 8888

ENTRYPOINT ["tini", "--"]
CMD ["start.sh", "/opt/notebook.sh"]


# Add files in the end to make most use of cache
ADD start.sh /usr/local/bin/
ADD build.sh /opt/bin/build
ADD test.sh /opt/bin/test
ADD notebook.sh /opt/
