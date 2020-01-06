FROM ubuntu
LABEL MAINTAINER parama86@gmail.com
COPY sample.sh /code/sample.sh
COPY testfile /code/testfile
RUN chmod +x /code/sample.sh
RUN echo "image is built...."
ENTRYPOINT ["sh","/code/sample.sh"]
CMD ["/code/testfile"]
