# In development, use the following to rebuild a completely fresh local copy for testing:
#
#   docker image rm thenetyeti/django:local ; docker system prune ; rm -rf engine
#   docker build --no-cache -t thenetyeti/django:local . 
#
# To log in and poke around within the container:
#   docker run -v ${PWD}/engine:/djangoproject --rm --name mysite -p 8001:8000 -u root -it thenetyeti/django:local bash
#
# For a test of the generators:
#   docker run -v ${PWD}/engine:/djangoproject --rm --name mysite -p 8001:8000 -it thenetyeti/django:local [create, createcms]

FROM python:3.6
LABEL maintainer="The NetYeti <netyeti@thenetyeti.com>"

# Some global environment settings
ENV PYTHONUNBUFFERED 1

# DEFAULT USER and GROUP ID
ARG UID=1000
ARG GID=1000

# Make sure the webengine port is available to other containers
EXPOSE 8000

# Set the target directory that we will be working in
ENV WRKDIR /djangoproject
WORKDIR ${WRKDIR}

# Setup user accounts and ensure this first bit is done as root
RUN mkdir -p /home/djangouser && \
    groupadd -g ${GID} djangouser && \
	useradd -M -r -u $UID -g ${GID} djangouser

# Get the container updated and install basline apps (and cleanup the mess to shrink the image)
RUN apt-get update && \
    apt-get install -y  --no-install-recommends \
        apt-utils \
        python3-dev \
        nano \
        git && \
    rm -rf /var/lib/apt/lists/*
	# may also want: apt-get install -y mysql-common libmysqlclient-dev python-mysqldb
RUN pip install --no-cache-dir --upgrade pip wheel gunicorn mysqlclient 

# Install the project files into the image
COPY ./src /src

# Add the command sauce
COPY ./bin /usr/local/bin/
RUN chmod +x /usr/local/bin/create* /usr/local/bin/gitinit


# Run the web engine creator! (default is vanilla Django - specify 'createcms' on the commandline for DjangoCMS installation)
CMD [ "create" ]
