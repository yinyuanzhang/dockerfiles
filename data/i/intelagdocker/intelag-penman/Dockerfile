# Dockerfile for light-weight data-filter
FROM openwhisk/dockerskeleton
 
ENV FLASK_PROXY_PORT 8080
#RUN pip install urllib2
#RUN apk -U upgrade && \
#  apk -U add python ca-certificates && \
#    update-ca-certificates
#RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
#RUN apk --no-cache --update-cache add gcc gfortran python python-dev py-pip build-base wget freetype-dev libpng-dev openblas-dev


RUN echo "http://dl-cdn.alpinelinux.org/alpine/v3.5/community" >> /etc/apk/repositories \
&& apk update \
&& apk add --update-cache --no-cache libgcc libquadmath musl \
&& apk add --update-cache --no-cache libgfortran \
&& apk add --update-cache --no-cache lapack-dev gcc gfortran python python-dev py-pip build-base wget freetype-dev libpng-dev

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN pip2.7 install numpy
RUN pip2.7 install pymongo

### Add source file(s)
ADD pennman.py /action/pennman.py
RUN rm /action/exec
ADD exec /action/
RUN chmod +x /action/exec

CMD ["/bin/bash", "-c", "cd actionProxy && python -u actionproxy.py"]
