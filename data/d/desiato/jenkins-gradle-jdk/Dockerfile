FROM desiato/jenkins-gradle
ADD jenkins-gradle.sh /usr/local/bin/
ADD sdkman-java-version.sh /usr/local/bin/
ENV ORIG_JAVA_HOME ${JAVA_HOME}
RUN source "$SDKMAN_DIR/bin/sdkman-init.sh" && sdk install java $(sdkman-java-version.sh)
