FROM busybox AS build-env
RUN wget https://releases.hashicorp.com/packer/1.2.4/packer_1.2.4_linux_amd64.zip
RUN unzip packer_1.2.4_linux_amd64.zip

FROM python:2
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY --from=build-env packer /usr/local/bin/packer
ENV USER avenuecode

CMD ["/bin/bash"]
