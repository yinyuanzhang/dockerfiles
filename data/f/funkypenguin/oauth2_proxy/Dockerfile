# Built following https://medium.com/@chemidy/create-the-smallest-and-secured-golang-docker-image-based-on-scratch-4752223b7324

# STEP 1 build executable binary
FROM golang:alpine as builder

# BUILD_DATE and VCS_REF are immaterial, since this is a 2-stage build, but our build
# hook won't work unless we specify the args
ARG BUILD_DATE
ARG VCS_REF

# BRANCH refers to the branch from the upstream we'll clone
# We use master instead of v2.2 since the self-signed-ssl patch is against master
#ARG BRANCH=v2.2
ARG BRANCH=master
ENV BRANCH=${BRANCH}

# Install SSL ca certificates (because we have to build the Go app with SSL support)
RUN apk update && apk add git && apk add ca-certificates

# Create appuser (so that this doesn't run as root)
RUN adduser -D -g '' appuser

# Check out the source
RUN git clone --branch $BRANCH https://github.com/bitly/oauth2_proxy.git $GOPATH/src/mypackage/myapp/ 
WORKDIR $GOPATH/src/mypackage/myapp/

# Apply the self-signed cert patch
RUN wget https://github.com/bitly/oauth2_proxy/pull/651/commits/3899576c07a51cf94307d679c76aafd72dcba4f2.patch
RUN patch -p1 < 3899576c07a51cf94307d679c76aafd72dcba4f2.patch

#get dependencies
RUN go get -d -v

#build the binary
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -installsuffix cgo -ldflags="-w -s" -o /go/bin/oauth_proxy


# STEP 2 build a small image
# start from scratch
FROM scratch

# Now we DO need these, for the auto-labeling of the image
ARG BUILD_DATE
ARG VCS_REF

# Good docker practice, plus we get microbadger badges
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/funkypenguin/oauth2_proxy.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="2.2-r1"

COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /etc/passwd /etc/passwd

# Copy our static executable
COPY --from=builder /go/bin/oauth_proxy /go/bin/oauth_proxy

EXPOSE 4080
USER appuser
ENTRYPOINT ["/go/bin/oauth_proxy"]
