# FROM node:10-alpine

# RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app
# ##create app directory to hold application code inside image
# WORKDIR /home/node/app
# # Install app dependencies
# # A wildcard is used to ensure both package.json AND package-lock.json are copied
# # where available (npm@5+)
# COPY package*.json ./

# # Bundle app source
# COPY . .

# #this app binds to port 3000 so this expose instruction maps the port with docker daemon
# EXPOSE 3000

# #apply migrations
# ENTRYPOINT ["./entrypoint.sh"]
# RUN ["chmod","755","./entrypoint.sh"]
FROM ubuntu:latest

ARG PYTHON_VERSION=3.7

RUN apt-get update && apt-get install -y --no-install-recommends \
         build-essential \
         cmake \
         curl \
         ca-certificates \
         libjpeg-dev \
         libpng-dev && \
     rm -rf /var/lib/apt/lists/*

RUN curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
     chmod +x ~/miniconda.sh && \
     ~/miniconda.sh -b -p /opt/conda && \
     rm ~/miniconda.sh && \
     /opt/conda/bin/conda install -y python=$PYTHON_VERSION numpy pyyaml scipy ipython mkl mkl-include ninja cython typing && \
     /opt/conda/bin/conda install -y pytorch-cpu torchvision-cpu -c pytorch && \
     /opt/conda/bin/conda clean -ya
ENV PATH /opt/conda/bin:$PATH

#For node
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash 
RUN apt-get -yq install nodejs

RUN /opt/conda/bin/conda install -y opencv rasterio

RUN yes | /opt/conda/bin/pip install gdal2tiles

RUN mkdir -p /home/app

WORKDIR /home/app

COPY package*.json ./

RUN npm install

COPY . .

RUN mkdir -p uploads
RUN mkdir -p analysisOutput
RUN mkdir -p public/tiles
RUN mkdir -p src/model

EXPOSE 3000

## Wait until mysql service has started
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
RUN chmod +x /wait

ENTRYPOINT ["./entrypoint.sh"]

