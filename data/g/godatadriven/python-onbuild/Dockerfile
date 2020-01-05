ARG MINICONDA_VERSION=3
FROM godatadriven/miniconda:${MINICONDA_VERSION}

LABEL org.label-schema.name="Python $MINICONDA_VERSION OnBuild PIP" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.version=$MINICONDA_VERSION

ONBUILD ADD requirements.txt packages.txt* build.sh* /dependencies/
ONBUILD RUN set -x\
            && apt-get update \
            && apt-get install -y gcc\
            && if [ -f /dependencies/packages.txt ]; then\
                apt-get install -y $(awk '/^\s*[^#]/' /dependencies/packages.txt | sed 's/\r//g');\
               fi\
            && pip install --no-cache-dir -r /dependencies/requirements.txt \
            && if [ -f /dependencies/build.sh ]; then\
                bash /dependencies/build.sh;\
               fi\
            && apt-get purge -y --auto-remove gcc \
            && apt-get clean

ENV PYTHONUNBUFFERED true
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
ENTRYPOINT ["python"]
CMD ["/app/main.py"]