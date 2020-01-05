FROM forumi0721/alpine-aarch64-base
ENV VERSION=3.6.5
RUN apk update \
    && apk --no-cache add wget unzip \
    && wget http://qiniu.zoranjojo.top/BaiduPCS-Go-${VERSION}-linux-arm64.zip \
    && unzip BaiduPCS-Go-${VERSION}-linux-arm64.zip \
    && mv BaiduPCS-Go-${VERSION}-linux-arm64/BaiduPCS-Go BaiduPCS-Go \
    && rm -rf BaiduPCS-Go-${VERSION}-linux-arm64*\	  
    && chmod a+x BaiduPCS-Go	  
VOLUME /Downloads
EXPOSE 5299
ENTRYPOINT ["./BaiduPCS-Go"]
