FROM microsoft/dotnet:2.2-aspnetcore-runtime

RUN apt-get update -qq && apt-get -y install libgdiplus libc6-dev wget xz-utils wkhtmltopdf && ln -s /usr/lib/libgdiplus.so /usr/lib/gdiplus.dll \
    && wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
    && tar vxf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && cp wkhtmltox/bin/wk* /usr/local/bin/