FROM node:4

ENV LOUNGE_VERSION 2.0.0-pre.4
ENV NODE_ENV production

ARG user=lounge
ARG group=lounge
ARG uid=1000
ARG gid=1000

ENV LOUNGE_HOME "/home/lounge"
ENV LOUNGE_DATA "${LOUNGE_HOME}/data"
ENV LOUNGE_SRC "${LOUNGE_HOME}/src"

# Create a non-root user for lounge to run in.
RUN groupadd --gid ${gid} ${group} \
 && useradd --home "${LOUNGE_HOME}" --create-home --uid ${uid} --gid ${gid} ${user}

RUN mkdir -p "${LOUNGE_DATA}"
RUN chown -R ${user}:${group} "${LOUNGE_DATA}"
VOLUME "${LOUNGE_DATA}"

# Drop root.
USER ${user}

# Install thelounge.
RUN mkdir -p "${LOUNGE_SRC}"
WORKDIR "${LOUNGE_SRC}"
RUN curl -L $(npm view thelounge@${LOUNGE_VERSION} dist.tarball) | tar --strip-components 1 -xzf -
RUN npm install

# Expose HTTP.
ENV PORT 9000
EXPOSE ${PORT}

ADD config.js /home/lounge/data/
ADD hashbang.css /home/lounge/src/client/themes/
ADD favicon.png /home/lounge/src/client/img/favicon-notification.png
ADD favicon.png /home/lounge/src/client/img/favicon.png

# Don't use an entrypoint here. It makes debugging difficult.
CMD node index.js --home "$LOUNGE_DATA"
