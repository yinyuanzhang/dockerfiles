FROM python:3.6-stretch

RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" > /etc/apt/sources.list.d/pgdg.list \
    && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        mysql-client \
        mongo-tools \
        postgresql-client-10 \
	&& rm -rf /var/lib/apt/lists/*

RUN wget "https://downloads.rclone.org/rclone-current-linux-amd64.deb" \
    && dpkg -i ./rclone-current-linux-amd64.deb \
    && rm ./rclone-current-linux-amd64.deb

COPY bin/ /app

RUN pip install requests

WORKDIR /app
CMD [ "/app/entrypoint.sh" ]
