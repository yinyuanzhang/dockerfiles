FROM golang:1.12.2-stretch

RUN mkdir /app 
ADD . /app/ 
WORKDIR /app 


RUN go get -u "github.com/boombuler/barcode"
RUN go get -u "github.com/boombuler/barcode"
RUN go get -u "github.com/dchest/uniuri"
RUN go get -u "github.com/fogleman/gg"
RUN go get -u "github.com/golang/freetype/truetype"
RUN go get -u "golang.org/x/image/font/gofont/goregular"

RUN CGO_ENABLED=1 GOOS=js GOARCH=wasm go get -u "github.com/dennwc/dom"
RUN CGO_ENABLED=1 GOOS=js GOARCH=wasm go get -u "syscall/js" 

RUN CGO_ENABLED=1 GOARCH=wasm GOOS=js go build -o test.wasm main.go

RUN CGO_ENABLED=1 GOARCH=amd64 GOOS=linux go build -o server server.go

EXPOSE 3000

CMD ["./server"]


