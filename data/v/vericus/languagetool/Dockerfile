FROM java:openjdk-8-jre-alpine

LABEL maintainer="Eamon Taaffe <eamon@cadmus.io>"

# You can specify any version listed here as a build arg:
# https://languagetool.org/download/. If you specify the version make sure you don't specify
# the release arg, because that will overide the version.
# Eg: `docker build --build-arg version=4.2`
ARG version=stable

# If you are going to be building a lot, download a server file into the current directory
# and specify the release as a build arg. This avoids the repeated downloading of the
# release file every time you need to build.
# Eg: `docker build --build-arg release=server.zip`
ARG release=https://languagetool.org/download/LanguageTool-${version}.zip

# Add the server file, unzip it and move it into and rename the directory so it is easier to
# refer to later.
ADD ${release} server.zip
RUN unzip server.zip && rm server.zip
RUN mv $(ls -d LanguageTool-*) server

# Move into the server directory, because this contains all the runtime stuff.
WORKDIR server

expose 80

# Note, this will throw runtime errors:
# - The server is being run in plain HTTP mode
# - The server is being run as the root user
CMD [ "java"                               \
    , "-cp", "languagetool-server.jar"     \
    , "org.languagetool.server.HTTPServer" \
    , "--port", "80"                       \
    , "--public"                           \
    ]
