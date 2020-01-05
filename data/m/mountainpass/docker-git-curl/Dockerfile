FROM docker/compose:1.24.0
RUN apk add --no-cache bash git openssh curl jq gettext
RUN envsubst --version
RUN git --version
RUN curl --version
RUN jq --version
RUN head --version || true
RUN cut --version || true
RUN docker --version
RUN docker-compose --version
