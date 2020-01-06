FROM java:8-jdk

RUN apt-get -y update && \
        apt-get -y install imagemagick

## PDFLib
RUN apt-get -qq install -y wget \
 && wget -O /tmp/pdflib.tar.gz "http://www.pdflib.com/binaries/PDFlib/910/PDFlib-9.1.0-Linux-x86_64-java.tar.gz" \
 && tar -zxf /tmp/pdflib.tar.gz -C /tmp "PDFlib-9.1.0-Linux-x86_64-java/bind/java/libpdflib_java.so" \ 
 && mv "/tmp/PDFlib-9.1.0-Linux-x86_64-java/bind/java/libpdflib_java.so" "/usr/lib/" \
 && rm -rf "/tmp/PDFlib-9.1.0-Linux-x86_64-java"

