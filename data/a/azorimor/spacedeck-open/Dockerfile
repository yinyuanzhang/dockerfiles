FROM node:10-alpine3.10
ENV NODE_ENV production
RUN apk update && \
    apk add ffmpeg ffmpeg-dev ghostscript ghostscript-dev make cmake g++ gcc boost boost-dev libmad libmad-dev gd gd-dev libgd libid3tag libid3tag-dev libsndfile libsndfile-dev git && \
    rm -Rf /var/cache/apk/* /var/lib/apk/* /etc/apk/cache/*

#RUN mkdir -p /deps
#WORKDIR /deps
#RUN git clone https://github.com/bbcrd/audiowaveform.git
#RUN mkdir -p /audiowaveform/build
#WORKDIR /audiowaveform/build
#RUN cmake -D ENABLE_TESTS=0 .. && make && make install

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install
RUN npm install -g gulp
RUN npm install gulp-rev-replace gulp-clean gulp-fingerprint gulp-rev gulp-rev-all gulp-sass gulp-concat
RUN npm install --only=dev
RUN npm link gulp


COPY spacedeck.js Dockerfile Gulpfile.js LICENSE /usr/src/app/
COPY config /usr/src/app/config
COPY helpers /usr/src/app/helpers
COPY locales /usr/src/app/locales
COPY middlewares /usr/src/app/middlewares
COPY models /usr/src/app/models
COPY public /usr/src/app/public
COPY routes /usr/src/app/routes
COPY styles /usr/src/app/styles
COPY views /usr/src/app/views

RUN /usr/local/bin/gulp styles
RUN npm cache verify

CMD [ "node", "spacedeck.js" ]

EXPOSE 9666
