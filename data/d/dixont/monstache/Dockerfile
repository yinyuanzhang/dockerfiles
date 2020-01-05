####################################################################################################
# Step 1: Build the app
####################################################################################################

FROM golang:alpine AS build-app

RUN apk add --no-cache gcc git musl-dev make zip
RUN apk update && apk add --no-cache ca-certificates && update-ca-certificates
RUN mkdir /app

WORKDIR /app

COPY . .

RUN go mod download

RUN make cgo

####################################################################################################
# Step 2: Copy output build file to an alpine image
####################################################################################################

FROM scratch
COPY --from=build-app /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=build-app /app/build/linux-amd64/monstache /bin/monstache
CMD ["/bin/monstache"]

