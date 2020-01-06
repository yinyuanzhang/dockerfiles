FROM python:3.7.1-slim-stretch

RUN apt-get update \
    && apt-get install wget bzip2 zip -y \
    && wget ftp://dicom.offis.de/pub/dicom/offis/software/dcmtk/dcmtk363/bin/dcmtk-3.6.3-linux-x86_64-static.tar.bz2 \
    && tar -jxf dcmtk-3.6.3-linux-x86_64-static.tar.bz2 \
    && mkdir /usr/local/dcmtk \
    && cp -r dcmtk-3.6.3-linux-x86_64-static/* /usr/local/dcmtk/ \
    && rm -rf dcmtk-3.6.3-linux-x86_64-static* \
    && chmod +x /usr/local/dcmtk/bin/* \
    && ln -s /usr/local/dcmtk/bin/* /usr/bin/

CMD ["python3"]