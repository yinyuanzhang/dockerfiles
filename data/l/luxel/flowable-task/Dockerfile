FROM maven:3-jdk-8-alpine
ENV BUILD_DIR /build-temp
ENV MODULE_DIR $BUILD_DIR/modules/flowable-ui-task

COPY ./ $BUILD_DIR/
WORKDIR $BUILD_DIR
RUN mvn -Pdistro clean install -DskipTests
WORKDIR $MODULE_DIR
RUN mvn -Pmysql clean package -DskipTests

FROM flowable/java8_server

ENV BUILD_DIR /build-temp
ENV MODULE_DIR $BUILD_DIR/modules/flowable-ui-task
ENV JAVA_OPTS=""

COPY --from=0 $MODULE_DIR/flowable-ui-task-app/target/flowable-task.war /app.war
COPY --from=0  $MODULE_DIR/flowable-ui-task-app/src/main/docker/wait-for-something.sh .
COPY --from=0 $MODULE_DIR/flowable-ui-task-app/src/main/docker/entrypoint.sh .
RUN chmod +x wait-for-something.sh
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]