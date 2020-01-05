FROM eclipse/ubuntu_jdk8

LABEL maintainer "IggySav"

ADD https://www.crushftp.com/early9/CrushFTP9_PC.zip /var/opt/ 

COPY run.sh /var/opt/ 

RUN sudo apt-get update 


RUN cd /var/opt/ \
    && sudo unzip CrushFTP9_PC.zip \
    && sudo chmod +x /var/opt/CrushFTP9_PC/crushftp_init.sh \
    && sudo chmod +x /var/opt/run.sh


WORKDIR /var/opt/CrushFTP9_PC/ 

RUN sudo java -jar CrushFTP.jar -a "admin" "admin"
    
EXPOSE 8080 443 21 2000-2010

CMD ["/var/opt/run.sh"]
