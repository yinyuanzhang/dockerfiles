## Imagen base
FROM golang:1.11.5
## Crea variables de entorno
# Estas variables permiten compilar el programa para una maquina con Windows
ENV GOOS=windows
ENV GOARCH=amd64
## Instala dependencias
# Instala node y sus dependencias
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
# Dependencias de paquetes de Go 
RUN go get github.com/gorilla/mux
RUN go get github.com/mattn/go-sqlite3
RUN go get github.com/tealeg/xlsx
## Agrega carpetade código
COPY . /$GOPATH/src/bitbucket.org/IslasGECI/gatos-trampas
WORKDIR /$GOPATH/src/bitbucket.org/IslasGECI/gatos-trampas
## Ejecuta makefile para compilar programa
CMD ["make", "mapa-gatos"]