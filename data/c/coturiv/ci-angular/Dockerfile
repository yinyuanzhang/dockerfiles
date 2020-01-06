FROM circleci/node:10-browsers
LABEL maintainer="coturiv@gmail.com"

# Install dependencies
RUN sudo npm i -g @angular/cli && \
    ng version && \
    sudo npm i -g firebase-tools