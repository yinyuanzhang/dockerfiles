FROM java:jre-alpine
MAINTAINER kongroo <imjcqt@gmail.com>
WORKDIR /root

COPY convert.sh /root/convert.sh
RUN apk add -U --no-cache wget unzip \
    && wget "https://drive.google.com/uc?export=download&id=1gFCTxte9gEu1VduGHo8fGqOe_YR7pfqV" -O Aozora.zip \
    && unzip Aozora.zip \
    && rm Aozora.zip \
    && mkdir books \
    && wget "http://www.amazon.co.jp/gp/redirect.html/ref=amb_link_8?location=http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz&token=321FBC360D6D2CE41E4ED829508B1F8017D89641&source=standards&pf_rd_m=AN1VRQENFRJN5&pf_rd_s=center-4&pf_rd_r=41CW6X7K3CBA1S4K8TQE&pf_rd_r=41CW6X7K3CBA1S4K8TQE&pf_rd_t=1401&pf_rd_p=2d215f9c-3454-475b-9a3a-957609cf4896&pf_rd_p=2d215f9c-3454-475b-9a3a-957609cf4896&pf_rd_i=3077677546" -O kindlegen.tgz \
    && tar zxvf kindlegen.tgz \
    && rm kindlegen.tgz \
    && apk del wget unzip --purge \
    && chmod +x convert.sh

CMD ["./convert.sh"]
