FROM fedora:30
RUN dnf update -y && dnf install -y npm
RUN npm install -g @angular/cli
COPY . /root/cloudztpui
RUN cd /root/cloudztpui && npm install
WORKDIR /root/cloudztpui
CMD ng serve --host 0.0.0.0
