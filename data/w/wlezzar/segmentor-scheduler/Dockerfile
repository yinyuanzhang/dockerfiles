FROM hseeberger/scala-sbt:8u131-jdk_2.12.2_0.13.15 as builder

COPY . /application

WORKDIR /application

RUN sbt clean universal:packageZipTarball

RUN tar -zxf target/universal/segmentor-scheduler-final.tgz -C / && \
    mv /segmentor-scheduler-final /segmentor-scheduler

####

FROM wlezzar/java:8

COPY --from=builder /segmentor-scheduler /segmentor-scheduler

ENTRYPOINT ["/segmentor-scheduler/bin/segmentor-scheduler"]