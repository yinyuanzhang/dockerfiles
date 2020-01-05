FROM ricklamers/gridstudio:release

ENV TZ=Asia/Shanghai

RUN apt-get install tzdata -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*