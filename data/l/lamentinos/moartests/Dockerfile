FROM circleci/android:api-25-node8-alpha

LABEL version="1.0.0" \
  maintainer="Stepan Beznosov" \
  maintainer.email="bez.stepan@gmail.com" \
  description="Moar tests" 


# setup project
RUN export ANDROID_HOME=/opt/android/sdk
RUN cd /tmp && git clone https://github.com/BStepan/stable-test.git
WORKDIR /tmp/stable-test
RUN rm -rf local.properties
RUN echo "sdk.dir=$ANDROID_HOME" > local.properties
RUN ./gradlew
RUN mkdir /tmp/reports
