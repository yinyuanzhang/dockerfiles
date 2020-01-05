
FROM imanzo/centos-go


RUN go get github.com/richardlehane/siegfried/cmd/sf 
RUN cd /go/src/github.com/richardlehane/siegfried
RUN sf -update
RUN sf -serve 0.0.0.0:513&
RUN yum install -y java
RUN cd /go
RUN git clone https://github.com/kidimanzo/springBoot.git && cd springBoot && git pull
RUN chmod +x /go/springBoot/launch.sh 
ENTRYPOINT /go/springBoot/launch.sh 
 
