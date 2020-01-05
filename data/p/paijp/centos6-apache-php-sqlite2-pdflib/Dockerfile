FROM paijp/centos6-apache-php-sqlite2

RUN \
	set -x &&\
	yum -y install gcc gcc-c++ php php-devel wget
RUN \
	set -x &&\
	mkdir -p /root/tmp &&\
	cd /root/tmp/ &&\
	wget 'https://web.archive.org/web/20060711133409/http://www.pdflib.com/products/pdflib/download/603src/PDFlib-Lite-6.0.3.tar.gz' &&\
	wget 'https://pecl.php.net/get/pdflib-2.1.7.tgz' &&\
	cd /root/tmp/ &&\
	tar xfz PDFlib-Lite-6.0.3.tar.gz &&\
	cd PDFlib-Lite-6.0.3 &&\
	./configure &&\
	make &&\
	make install &&\
	ldconfig /usr/local/lib &&\
	cd /root/tmp/ &&\
	tar xfz pdflib-2.1.7.tgz &&\
	cd pdflib-2.1.7 &&\
	phpize &&\
	./configure &&\
	make &&\
	make install &&\
	ldconfig /usr/local/lib &&\
	cd /root/ &&\
	rm -fr tmp &&\
	echo 'extension=pdf.so' >/etc/php.d/libpdf.ini

EXPOSE 80 443
CMD php -i |grep PDF

