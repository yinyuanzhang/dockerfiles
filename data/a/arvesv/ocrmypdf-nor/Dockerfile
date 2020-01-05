FROM jbarlow83/ocrmypdf

ENV DEBIAN_FRONTEND noninteractive
# Add Norwegian
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y --no-install-recommends tesseract-ocr-nor
