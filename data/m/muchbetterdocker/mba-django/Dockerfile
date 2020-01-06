# Docker container to run our main django site - just installs the bits needed on top of the heroku:16 image
FROM heroku/heroku:16

RUN apt-get update && apt-get -y install python-pip --fix-missing
RUN apt-get update && apt-get install -y libmemcached-dev zlib1g-dev libssl-dev --fix-missing
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin --fix-missing
RUN apt-get update && apt-get install -y libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk  --fix-missing
RUN apt-get update && apt-get install -y libpq-dev --fix-missing
ENV PYTHONUNBUFFERED 1
