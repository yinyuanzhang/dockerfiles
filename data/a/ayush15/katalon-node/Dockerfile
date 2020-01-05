FROM ayush15/katalon-base

ARG KATALON_STUDIO_VERSION

# common environment variables
ENV KATALON_KATALON_ROOT_DIR=$KATALON_ROOT_DIR/katalon
ENV KATALON_KATALON_INSTALL_DIR_PARENT=/opt
ENV KATALON_KATALON_INSTALL_DIR=$KATALON_KATALON_INSTALL_DIR_PARENT/katalonstudio

# copy scripts
RUN mkdir -p $KATALON_KATALON_ROOT_DIR
WORKDIR $KATALON_KATALON_ROOT_DIR
ADD katalon/src ./

RUN $KATALON_MAKE_EXECUTABLE_SCRIPT .

RUN ./index.sh
RUN $KATALON_CLEAN_UP_SCRIPT

ENV PATH "$PATH:$KATALON_KATALON_ROOT_DIR/scripts"

# install node
USER root
RUN apt-get update
RUN apt-get -y install curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_11.x  | bash -
RUN apt-get -y install nodejs
RUN npm install

WORKDIR /

CMD $KATALON_KATALON_ROOT_DIR/scripts/katalon-notify.sh