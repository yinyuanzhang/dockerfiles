FROM golang as builder
COPY . /go/src/github.com/arisau/locon
WORKDIR /go/src/github.com/arisau/locon
#get dependancies
RUN go get -d -v
#build the binary
RUN CGO_ENABLED=0 go build -a --installsuffix cgo --ldflags="-s" -o locon .
# STEP 2 build a small image
# start from scratch
FROM iron/base
# Copy our static executable
COPY --from=builder /go/src/github.com/arisau/locon/locon /app/locon
COPY --from=builder /go/src/github.com/arisau/locon/templates /app/templates
COPY --from=builder /go/src/github.com/arisau/locon/static /app/static
ENTRYPOINT ["/app/locon"]