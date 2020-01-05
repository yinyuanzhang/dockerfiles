FROM node:10
ADD ./src/install/ $INST_SCRIPTS/
RUN find $INST_SCRIPTS -name '*.sh' -exec chmod a+x {} +
RUN $INST_SCRIPTS/setup.sh


CMD [ "node" ]
