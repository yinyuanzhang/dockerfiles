FROM java:7-jdk
MAINTAINER Rui Gonçalves <ruippeixotog@gmail.com>

RUN apt-get update
RUN apt-get install -y ipython-notebook git

RUN git clone https://github.com/mattpap/IScala.git
RUN cd IScala && ./sbt assembly
RUN cp IScala/target/scala-2.11/lib/IScala.jar /IScala.jar
RUN mkdir /notebooks

EXPOSE 8888
VOLUME /notebooks

WORKDIR /notebooks
CMD /usr/bin/ipython notebook --ip=* \
  --KernelManager.kernel_cmd='["java", "-jar", "/IScala.jar", "--connection-file", "{connection_file}", "--parent"]'
