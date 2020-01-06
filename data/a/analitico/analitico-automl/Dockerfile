# docker hub will build analitico:analitico-automl automatically from this repository
FROM tensorflow/tfx:0.15.0

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# Copy environment.yml (if found) to a temp locaition so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
COPY environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/

# Copy tfx/automl pipelines source code and demo data
COPY source /root/source
COPY data /root/data

ENV PYTHONPATH "${PYTHONPATH}:/root/source"

# Configure apt and install packages
RUN apt-get update \
    && python -V \
    && apt-get -y install --no-install-recommends apt-utils dialog 2>&1 \
    #
    # Verify git, process tools, lsb-release (common in install instructions for CLIs) installed
    && apt-get -y install git iproute2 procps iproute2 lsb-release \
    #
    # We start from the Tensorflow Extended docker file so we already
    # have tfx, tfx-bsl, tensorflow, tensorflow-metadata, tensorflow-transform, ml-metadata, 
    # tensorboard and more, see Compatible versions: https://pypi.org/project/tfx/
    # We add a few more packages used by Visual Studio or our specific pipelines
    && pip install pylint \
    && pip install pytest \
    && pip install psutil \
    && pip install black \
    && pip install absl-py \
    && pip install python-snappy \
    && pip install kfp==0.1.37 \
    && pip install networkx \
    && pip install matplotlib \
    #
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=
