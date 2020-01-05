FROM mysql:5.6
COPY setup.sh /mysql/setup.sh
COPY setup.sql /mysql/setup.sql
RUN chmod +x /mysql/setup.sh
RUN /mysql/setup.sh