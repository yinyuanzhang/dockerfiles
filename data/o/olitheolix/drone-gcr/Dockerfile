# ----------------------------------------------------------------------
# Stage 1: Install docker-credential-gcr into temporary container.
# ----------------------------------------------------------------------
# We will copy the credentials helper from Google's official SDK.
FROM google/cloud-sdk:alpine as builder

RUN gcloud components install docker-credential-gcr --quiet
RUN docker-credential-gcr version


# ----------------------------------------------------------------------
# Stage 2: Create container that Drone can use its pipeline.
# ----------------------------------------------------------------------
FROM alpine:3.6

# Essentials.
RUN apk --no-cache add libc6-compat docker

# Copy Google's Docker Credentials Helper from the first build stage and
# let configure itself for use with Docker.
COPY --from=builder /google-cloud-sdk/bin/* /usr/local/bin/
RUN docker-credential-gcr configure-docker

# Spawn a shell by default.
ENTRYPOINT ["/bin/ash"]
