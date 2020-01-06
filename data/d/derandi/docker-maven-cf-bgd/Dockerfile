FROM maven:3-jdk-8

ENV CF_CLI_VERSION "6.40.0"
ENV CF_BGD_VERSION "1.4.0"
ENV CF_BGD_CHECKSUM "a2901bf17a030c8f58b6622c855f775dfebd3f239dba1737b4bc2de18307db03"
ENV CF_BGD_TEMPFILE "/tmp/blue-green-deploy.linux64"

#Needed to add key for cf-cli
RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-transport-https

#Install cf-cli
#https://docs.cloudfoundry.org/cf-cli/install-go-cli.html
RUN wget -q -O - https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | apt-key add -
RUN echo "deb http://packages.cloudfoundry.org/debian stable main" | tee /etc/apt/sources.list.d/cloudfoundry-cli.list
RUN apt-get update
RUN apt-get install -y --no-install-recommends cf-cli

RUN curl -L -o "${CF_BGD_TEMPFILE}" \
  "https://github.com/bluemixgaragelondon/cf-blue-green-deploy/releases/download/v${CF_BGD_VERSION}/blue-green-deploy.linux64" \
  && echo "${CF_BGD_CHECKSUM}  ${CF_BGD_TEMPFILE}" | sha256sum -c - \
  && chmod +x "${CF_BGD_TEMPFILE}" \
  && cf install-plugin -f "${CF_BGD_TEMPFILE}" \
  && rm "${CF_BGD_TEMPFILE}"
  
WORKDIR /tmp/
COPY rollback.sh rollback.sh
