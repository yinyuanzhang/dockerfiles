FROM eyesfree/todobackend-base:latest
LABEL application="todobackend"

# Commented out to be buildable in Jenkins and Docker Hub
# ENV http_proxy "http://172.17.0.1:3128"
# ENV https_proxy "http://172.17.0.1:3128"

# Install dev and build dependencies
RUN apt-get update && \
apt-get install -qy python-dev libmysqlclient-dev \
build-essential libssl-dev libffi-dev \
libxml2-dev libxslt1-dev zlib1g-dev \
python-pip

# Activate virtual environment and install wheel support
RUN . /appenv/bin/activate && \
pip install --upgrade pip && \
pip install wheel --upgrade

# must be set after installing wheel
ENV WHEELHOUSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache 

# Output directory: Build cache
VOLUME /wheelhouse

# Output directory: Build artefacts (Wheels) are output here
VOLUME /build

# Output directory: Test reports are output here
VOLUME /test-reports

# Add test entrypoint script from this projet
COPY scripts/test.sh /usr/local/bin/test.sh
RUN chmod +x /usr/local/bin/test.sh

# Override the entrypoint from the base image. The script from the base image cann still be used.
ENTRYPOINT ["test.sh"]
# CMD ["python", "manage.py", "test", "--settings=todobackend.settings.test", "--noinput"]
CMD ["python", "manage.py", "test", "--noinput"]


# Add application soure to /application directory and use it. 
# Written last because the source code will be change most often - the rest 
# of the layers can then be reused from cache.
COPY src /application
WORKDIR /application