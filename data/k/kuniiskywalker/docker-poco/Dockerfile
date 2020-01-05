FROM gcc:4.9

COPY ./poco-1.7.8p3-all.tar.gz /usr/src/
RUN tar xzfv /usr/src/poco-1.7.8p3-all.tar.gz -C /usr/src
WORKDIR /usr/src/poco-1.7.8p3-all
RUN ./configure --no-tests --no-wstring --omit=Data/SQLite,Data/MySQL,Data/ODBC,Zip,MongoDB,PageCompiler,PageCompiler/File2Page
RUN make
RUN make install
RUN ldconfig

WORKDIR /usr/src
RUN rm -rf /usr/src/poco-1.7.8p3-all
