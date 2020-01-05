FROM ubuntu:18.04

ARG SHEEPIT_JAR_URL="https://www.sheepit-renderfarm.com/media/applet/client-latest.php"
ARG BUILD_VERSION
ARG VCS_REF
ARG BUILD_DATE
ARG DOCKER_TAG

ENV WORKDIR "/app"
ENV SHEEPIT_JAR_FILENAME "sheepit.jar"
ENV SHEEPIT_USER "D3lta"
ENV SHEEPIT_TOKEN "ZSQko2QvmU7wbaoKZZr1YnPmV6MdCzfTpAImpGRw"
ENV SHEEPIT_CORES "4"
ENV SHEEPIT_CACHE "/tmp"
ENV SHEEPIT_MEM "4G"
ENV SHEEPIT_SERVER "https://client.sheepit-renderfarm.com"

WORKDIR ${WORKDIR}
ADD entrypoint.sh .
RUN chmod +x entrypoint.sh

RUN apt update && \
	apt install -y --no-install-recommends \
		wget \
		bzip2 \
		libfreetype6 \
		libgl1-mesa-dev \
		libglu1-mesa \
		libxi6 \
		libxrender1 \
		software-properties-common \
		default-jre-headless && \
	apt autoremove -y && \
	apt autoclean && \
rm -rf /var/lib/apt/lists/* /tmp/* && \
wget -O ${WORKDIR}/${SHEEPIT_JAR_FILENAME} ${SHEEPIT_JAR_URL} && \
java -jar ${WORKDIR}/${SHEEPIT_JAR_FILENAME} --version

CMD ["/app/entrypoint.sh"]
