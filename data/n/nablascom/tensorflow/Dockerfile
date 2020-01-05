FROM tensorflow/tensorflow:latest-gpu-py3-jupyter
ARG NODEJS_VERSION=node_12.x

RUN curl -fsSL "https://deb.nodesource.com/gpgkey/nodesource.gpg.key" | apt-key add - && \
	add-apt-repository "deb https://deb.nodesource.com/$NODEJS_VERSION $(lsb_release -sc) main" && \
	apt-get update && \
	env DEBIAN_FRONTEND=noninteractive apt-get install sudo nodejs --no-install-recommends -y

RUN pip install --no-cache-dir jupyterlab jupyterhub jupyter_tensorboard && \
	jupyter labextension install jupyterlab_tensorboard \
	@jupyter-widgets/jupyterlab-manager \
	@jupyterlab/toc  \
	jupyter-matplotlib -y --clean && \
	jlpm cache clean
