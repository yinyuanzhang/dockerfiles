#Converting from MTA server dockerfile
FROM odegay/oxota_server_base:latest

#RUN apt-get update && apt-get upgrade -y

COPY samp-install.sh /app/

RUN chmod a+x /app/samp-install.sh

RUN bash /app/samp-install.sh

EXPOSE 7777

WORKDIR "/samp03"

#CMD ["./samp03svr"]

CMD ["/bin/bash"]
