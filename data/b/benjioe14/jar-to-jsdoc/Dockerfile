FROM java
WORKDIR /usr/local/bin/dts-generator
COPY ./dts-generator/gradle ./gradle
COPY ./dts-generator/build.gradle ./dts-generator/gradlew ./

RUN ./gradlew build

COPY ./dts-generator/src ./src
RUN ./gradlew jar


ENTRYPOINT [ "java", "-jar", "build/libs/dts-generator.jar" ]
CMD ["-input", "/usr/src/jarFolder", "-output", "/usr/src/jarFolder/dts"]b