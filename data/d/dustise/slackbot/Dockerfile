FROM alpine
COPY prepare.sh /usr/local/bin
COPY entry.sh /usr/local/bin
ENV REPOSITORY="k8smeetup/website-tasks" \
    RESULT_COUNT=5 \
    LOCAL_REPO="k8s-1.2/repo" \
    SLACK_ADMINS="@admin" \
    BOT_TOKEN="" \
    ORG="" \
    GITHUB_THRESHOLD=100 \
    OUTPUT_THRESHOLD=100
RUN /usr/local/bin/prepare.sh
COPY supervisord.conf /etc/
COPY src /src
WORKDIR /errbot
VOLUME ["/errbot", "/repo"]
CMD ["/usr/local/bin/entry.sh"]
