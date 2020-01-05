# Install Polymer CLI, https://www.polymer-project.org/3.0/docs/tools/polymer-cli
FROM node

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	   git \
	&& rm -rf /var/lib/apt/lists/*

RUN npm install -g polymer-cli --unsafe-perm

EXPOSE 8080
EXPOSE 8081

WORKDIR "/workspace/external"
COPY data/dot_bashrc /root/.bashrc
