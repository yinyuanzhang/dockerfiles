# REQUIRED ENV
# OS: ubuntu (16.04 LTS or higher)
# Python: 3.6
# Flask: newest
# uwsgi: newest
# cmake

# base on python 3.6
FROM python:3.6
RUN python --version
RUN pip3 --version

# install common packages
RUN apt-get update
RUN apt-get install -y cmake \
	libxrender1 \
	libsm6 \
	libxext6 \
	build-essential

# install flask packages
RUN pip3 install flask \
	flask_socketio \
	flask_cors
	
# setup uwsgi
RUN pip3 install uwsgi
