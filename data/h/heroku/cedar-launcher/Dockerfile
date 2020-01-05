FROM heroku/heroku:18-build

RUN curl --fail --retry 3 -L -o /tmp/log-shuttle.deb https://github.com/heroku/log-shuttle/releases/download/v0.17.1/log-shuttle_0.17.1_amd64.deb && dpkg -i /tmp/log-shuttle.deb && rm /tmp/log-shuttle.deb
ADD https://heroku-dan-bucket.s3.amazonaws.com/rendezvous-run-linux-amd64.gz /tmp
RUN gunzip /tmp/rendezvous-run-linux-amd64.gz && chmod +x /tmp/rendezvous-run-linux-amd64 && mv /tmp/rendezvous-run-linux-amd64 /usr/bin/rendezvous-run
ADD bin/setuser /sbin/setuser
ADD bin/entrypoint /usr/bin/entrypoint
RUN useradd -m app -d /app

ENTRYPOINT ["/sbin/setuser", "app", "/usr/bin/entrypoint"]
