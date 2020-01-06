FROM java:latest

ADD https://github.com/google/closure-stylesheets/releases/download/v1.5.0/closure-stylesheets.jar closure-stylesheets.jar
ADD https://dl.google.com/closure-compiler/compiler-20181008.zip compiler-20181008.zip
RUN unzip compiler-20181008.zip
RUN mv closure-compiler-v20181008.jar closure-compiler.jar