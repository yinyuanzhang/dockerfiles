FROM python:3.7-alpine3.9

# written by: Oliver Cordes 2019-06-24
# changed by: Oliver Cordes 2019-06-27


RUN adduser -D rayqueue

WORKDIR /home/rayqueue

RUN apk add --update  --no-cache \
	git gcc libc-dev linux-headers


RUN python -m venv venv


RUN git clone https://github.com/ocordes/rayqueue.git

RUN cd rayqueue && rm -rf src/ Dockerfile* docker-compose.yml requirements.dat README.md boot.sh

RUN venv/bin/pip install --no-cache-dir psutil requests

RUN cd rayqueue/client/ && ../../venv/bin/pip install --no-cache-dir .


FROM python:3.7-alpine3.9

# add the rayqueue user
RUN adduser -D rayqueue

# copy from previous build
COPY --from=0 /home /home

COPY --from=ocordes/povray:3.7-stable  /usr/local /usr/local
COPY --from=ocordes/povray:3.7-stable  /root/.povray /home/rayqueue/.povray


RUN apk add --update  --no-cache \
    boost \
    zlib \
    libpng \
    tiff \
    sdl \
    ilmbase \
    openexr  \
    git && \
    rm -rf /var/cache/apk*


RUN touch /rayqueue.ini

# we are now in our home
WORKDIR /home/rayqueue

COPY run.sh .
RUN chmod 755 run.sh

RUN ln -s /rayqueue.ini rayqueue/client-test/rayqueue.ini

RUN chown -R rayqueue:rayqueue ./

USER rayqueue


#ENTRYPOINT ["/bin/sh"]
ENTRYPOINT ["./run.sh"]


