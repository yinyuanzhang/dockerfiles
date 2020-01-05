FROM capside/nodejs:v4.1.0
MAINTAINER Roi Ares <roi.ares@consultorestic.pro>


RUN wget https://bitbucket.org/roiares/pruebas/raw/95ef5a0d98276474e9a0cf722844dba6eb1ee407/webservice.js \ 
    --no-check-certificate 

#A linked container could access to this port
EXPOSE 8888

CMD ["/node/bin/node", "webservice.js"] 