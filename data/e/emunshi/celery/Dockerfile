#
# Celery Dockerfile
#
# https://github.com/emunshi/celery
#

# Pull base image.
FROM emunshi/python

# Install Celery.
RUN pip install celery
# Install flower to manage celery
RUN pip install flower

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["bash"]
