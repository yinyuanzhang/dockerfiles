FROM debian:stretch
MAINTAINER Jacopo Mauro

RUN apt-get update && \
	apt-get install -y \
 		wget \
 		unzip \
 		xz-utils && \
	rm -rf /var/lib/apt/lists/* && \
  mkdir /tool && \
	cd /tool && \
	wget --no-check-certificate http://ie.technion.ac.il/~ofers/HCSP/hcsp-1.3.0-x86_64.tar.xz && \
	tar -xJf hcsp-1.3.0-x86_64.tar.xz && \
	mv hcsp-1.3.0-x86_64 haifacsp && \
	rm -rf hcsp-1.3.0-x86_64.tar.xz && \
	cd haifacsp && \
	wget --no-check-certificate http://strichman.net.technion.ac.il/files/2016/07/hcsp-mzn-lib.tar_.zip && \
	unzip hcsp-mzn-lib.tar_.zip && \
	mv hcsp-mzn-lib.tar mzn-lib && \
	rm -rf mzn-lib/hcsp-mzn-lib* ../hcsp-mzn-lib.tar_.zip && \
	echo '#!/bin/bash\n\
HERE=`dirname "$(readlink -f ${BASH_SOURCE[0]})"`\n\
$HERE/hcsp.big -F fzn "$@"' > /tool/haifacsp/fzn-haifacsp && \
	chmod 700 /tool/haifacsp/fzn-haifacsp
	
ENV PATH "$PATH:/tool/haifacsp/"

# minizinc lib files in /tool/haifacsp/mzn-lib
# solver /tool/haifacsp/fzn-haifacsp
