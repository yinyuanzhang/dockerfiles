FROM alpine
MAINTAINER Patrick Fruh <patrick@kaeltis.de>

RUN \
	apk --no-cache add \
		ca-certificates \
		openssl \
		perl \
		perl-doc \
		mariadb-client \
	&& update-ca-certificates \
	&& wget https://raw.githubusercontent.com/major/MySQLTuner-perl/master/mysqltuner.pl -O mysqltuner.pl \
	&& wget https://raw.githubusercontent.com/major/MySQLTuner-perl/master/basic_passwords.txt -O basic_passwords.txt \
	&& wget https://raw.githubusercontent.com/major/MySQLTuner-perl/master/vulnerabilities.csv -O vulnerabilities.csv

ENTRYPOINT ["perl", "mysqltuner.pl"]
CMD ["--help"]
