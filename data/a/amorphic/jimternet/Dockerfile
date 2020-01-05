FROM python:3.7 AS builder
ENV PYTHONUNBUFFERED 1

ENV BUILD_DIR /jimternet
ENV CONTENT_DIR ${BUILD_DIR}/content
ENV OUTPUT_DIR ${BUILD_DIR}/output

ENV SETTINGS_FILE ${BUILD_DIR}/publishconf.py
ENV GIT_REPO https://github.com/amorphic/jimternet.git
ENV GIT_BRANCH master
ENV PLUGINS_DIR ${BUILD_DIR}/plugins
ENV PLUGINS_REPO https://github.com/getpelican/pelican-plugins
ENV THEMES_DIR ${BUILD_DIR}/themes
ENV THEMES_REPO https://github.com/getpelican/pelican-themes

RUN mkdir $BUILD_DIR
RUN git clone -b $GIT_BRANCH $GIT_REPO $BUILD_DIR
RUN git clone --recursive $PLUGINS_REPO $PLUGINS_DIR
# Pending changes to amorphic/attila being pushed upstream
RUN mkdir $THEMES_DIR
RUN git clone -b add_continue_reading https://github.com/amorphic/attila ${THEMES_DIR}/attila
##RUN git clone --recursive $THEMES_REPO $THEMES_DIR

WORKDIR $BUILD_DIR
RUN pip install -r ${BUILD_DIR}/requirements.txt
RUN pelican-themes -i ${THEMES_DIR}/*

RUN pelican -o $OUTPUT_DIR -s $SETTINGS_FILE $CONTENT_DIR

FROM nginx AS deploy
LABEL com.centurylinklabs.watchtower.enable="true"
ENV BUILD_DIR /jimternet
ENV OUTPUT_DIR ${BUILD_DIR}/output
COPY --from=builder ${OUTPUT_DIR} /usr/share/nginx/html/
