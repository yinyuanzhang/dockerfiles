FROM gittools/gitversion:5.0.0-beta2-65-linux
WORKDIR /app
RUN apt install -y jq
COPY pipe /
RUN chmod a+x /*.sh
VOLUME /src
ENTRYPOINT ["/pipe.sh"]
