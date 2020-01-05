FROM piperbuilder/ubuntu-builder

ARG SOURCE_COMMIT
ARG SOURCE_BRANCH

WORKDIR /home/piper/piper-story
COPY . ./

# Generate version hash
RUN echo "$SOURCE_COMMIT" > version.hash

CMD [ "bash" ]
