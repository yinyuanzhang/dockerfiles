# STAGE0
FROM dialogexe/ciset:latest as builder

LABEL Christian Sakshaug <christian@dx.no>

RUN mkdir /o
RUN mkdir /o/ci
RUN mkdir /o/app
RUN mkdir /o/tpl
RUN cp -R /ci/* /o/ci
COPY entrypoint.sh /o/entrypoint.sh
COPY scripts /o/ci/scripts
COPY tpl /o/ci/tpl
RUN chmod +x /o/entrypoint.sh
RUN chmod +x /o/ci/scripts/*.sh
RUN chmod 644 /o/ci/tpl/*

# STAGE1
FROM microsoft/dotnet:latest
# COPY FROM STAGE0 SO WE DONT TAKE WITH SECRETS
COPY --from=builder /o/. /

#RUN apt-get update && apt-get install -y vim

WORKDIR /app

CMD /entrypoint.sh