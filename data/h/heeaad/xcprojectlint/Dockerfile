FROM norionomura/swift:412
LABEL maintainer "Steffen Matthischke <steffen.matthischke@gmail.com>"

ENV BRANCH="master"

RUN git clone --branch $BRANCH https://github.com/americanexpress/xcprojectlint && \
    cd xcprojectlint && \
    swift package update && \
    swift build --configuration release && \
    mv `swift build --configuration release --show-bin-path`/xcprojectlint /usr/bin && \
    cd .. && \
    rm -rf xcprojectlint

# Print Installed xcprojectlint Version
RUN xcprojectlint --version
CMD ["xcprojectlint"]
