FROM boileaum/jupyter

# From Jupyter Project <jupyter@googlegroups.com>

LABEL maintainer="Matthieu Boileau <matthieu.boileau@math.unistra.fr>"

USER root

RUN apt-get update && apt-get -yq dist-upgrade \
 && apt-get install -yq --no-install-recommends \
    libpocl-dev \
    opencl-headers \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/lib/x86_64-linux-gnu/libOpenCL.so.1 /usr/lib/libOpenCL.so

# Switch back to NB_USER to avoid accidental container runs as root
USER $NB_USER
ADD requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt
WORKDIR $HOME/work
