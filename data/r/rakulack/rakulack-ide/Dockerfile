FROM centos:7
RUN curl -sL https://rpm.nodesource.com/setup_10.x | bash -
RUN yum install yum install -y nodejs gcc-c++ make
RUN yum install -y epel-release
RUN yum install -y golang
RUN go get github.com/thestrukture/IDE
RUN go get github.com/cheikhshift/gos
RUN cd root/go/src/github.com/thestrukture/IDE/ui ;npm install
EXPOSE 8884
ENTRYPOINT ["/root/go/bin/IDE","--headless","&","npm start"]
CMD ["-p","80:8884"]
