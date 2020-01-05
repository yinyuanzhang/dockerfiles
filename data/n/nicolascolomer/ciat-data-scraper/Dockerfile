FROM balenalib/raspberry-pi

RUN [ "cross-build-start" ]

# Install package
RUN apt-get update \
&&  apt-get install -y build-essential debhelper dh-systemd dh-virtualenv \
&&  apt-get install -y python3-pip python3-dev python3-setuptools \
&&  apt-get install -y libopencv-dev libatlas-base-dev libjasper-dev libgstreamer1.0-dev libgtk-3-dev

# Setup environment
COPY . /ciat-data-scraper
WORKDIR /ciat-data-scraper
ENV LC_ALL=C.UTF-8 LANG=C.UTF-8
RUN pip3 install pipenv
RUN pipenv install --dev --system --three

CMD /bin/bash
