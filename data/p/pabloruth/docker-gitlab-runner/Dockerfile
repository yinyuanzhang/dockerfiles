FROM debian:stretch-slim

RUN apt-get update && apt-get install -y wget && wget -O /usr/local/bin/gitlab-runner https://gitlab-runner-downloads.s3.amazonaws.com/v10.4.0/binaries/gitlab-runner-linux-amd64 && wget -O /usr/local/bin/go-init https://gitlab.com/pablo-ruth/go-init/-/jobs/38844065/artifacts/raw/go-init && apt-get remove -y --purge wget && apt-get clean all -y

COPY register.sh unregister.sh /

RUN chmod +x /usr/local/bin/gitlab-runner /usr/local/bin/go-init /register.sh /unregister.sh

RUN useradd --comment 'GitLab Runner' --create-home gitlab-runner --shell /bin/bash

ENTRYPOINT ["/usr/local/bin/go-init"]
CMD ["-pre", "/register.sh", "-main", "gitlab-runner run --user=gitlab-runner --working-directory=/home/gitlab-runner", "-post", "/unregister.sh"]
