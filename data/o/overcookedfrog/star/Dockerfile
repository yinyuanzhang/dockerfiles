FROM centos:7 as builder
RUN yum install -y zlib-devel bzip2-devel xz-devel libcurl-devel ncurses-devel gcc openssl-devel make bzip2
WORKDIR /samtools
RUN curl -L https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 | tar xj --strip-components=1
RUN ./configure && make && make install
WORKDIR /star
RUN curl -L https://github.com/alexdobin/STAR/archive/2.7.0f.tar.gz | tar xz --strip-components=1

FROM centos:7
RUN yum install -y zlib bzip2 xz libcurl ncurses openssl
COPY --from=builder /star/bin/Linux_x86_64_static/STAR /usr/local/bin/STAR
COPY --from=builder /star/bin/Linux_x86_64_static/STARlong /usr/local/bin/STARlong
COPY --from=builder /usr/local/bin/samtools /usr/local/bin/samtools
