FROM scarecrowddb/pythonbase-nmap:20191030.01

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

# Now copy in our code, and run it
COPY . /app


RUN pip3 install -r requirements.txt \
    && echo $(TZ=Australia/Brisbane date +"Version: %Y%m%d.%H%M%S") > /app/version.txt \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && locale-gen \
    && chmod +x /app/files/startup.sh \
    && mkdir -p /var/www \
    && touch /var/www/testfile.txt \
    && export PYMSSQL_BUILD_WITH_BUNDLED_FREETDS=1 \
    && pip3 install pymssql

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

CMD tail -f /dev/null

#ENTRYPOINT  ["/app/files/startup.sh"]
