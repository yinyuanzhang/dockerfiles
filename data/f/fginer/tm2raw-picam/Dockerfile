from williamyeh/java8
RUN mkdir -p /picam
RUN mkdir /picam/spice
RUN mkdir /picam/data
WORKDIR /picam
COPY picam.tar.gz /picam/
RUN tar -zxvf /picam/picam.tar.gz
#RUN mv /picam/iwf-tm2raw-picam-1.4.0 /picam/tm2raw
RUN rm -f /picam/picam.tar.gz
COPY tm2raw.properties /picam/tm2raw/conf/
COPY raw2cal.properties /picam/tm2raw/conf/
RUN apt-get update
RUN apt-get -y install joe


#from fiadliel/java8-jre
#RUN mkdir -p /picam
#RUN mkdir /picam/spice
#RUN mkdir /picam/data
#WORKDIR /picam
#COPY picam.tar.gz /picam/
#RUN tar -zxf /picam/picam.tar.gz
#RUN mv /picam/iwf-tm2raw-picam-1.4.0 /picam/tm2raw
#RUN rm -f /picam/picam.tar.gz
#COPY tm2raw.properties /picam/tm2raw/conf/
#COPY raw2cal.properties /picam/tm2raw/conf/
#RUN apk update
#RUN apk add joe





#to create the container with host directories mapped to container directories do following:
#copy spice kernel directory to d:/docker/spice
#docker run --rm -v /d/temp/tm2raw:/picam/data/ -v /d/docker-data/spice/kernels:/picam/spice -it [image] bash
#docker run --rm -v /d/temp/tm2raw:/picam/data/ -v /d/docker-data/spice/kernels:/picam/spice fginer/tm2raw-picam:1.3.0 /picam/tm2raw/bin/tm2raw-picam