FROM muicoder/glibc

ENV ANDROID_HOME=/opt

ENV PATH=$ANDROID_HOME/platform-tools:$PATH

RUN mkdir -pm 0750 ~/.android $ANDROID_HOME \
    && curl -fsSL https://dl.google.com/android/repository/platform-tools-latest-linux.zip \
        -o /tmp/adb.zip ; unzip /tmp/adb.zip -d $ANDROID_HOME \
    && curl -sSL https://github.com/muicoder/adb/raw/master/entrypoint.sh \
        -o /sbin/entrypoint.sh ; chmod +x /sbin/entrypoint.sh && \
    rm -rf /tmp/*

EXPOSE 5037

ENTRYPOINT ["tini", "-s", "--", "entrypoint.sh"]

CMD ["adb", "-a", "-P", "5037", "server", "nodaemon"]
