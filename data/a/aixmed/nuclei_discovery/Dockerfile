FROM rainbean/tensor:latest as builder
ADD . /src
WORKDIR /src
RUN python setup.py bdist_egg --exclude-source-files

FROM rainbean/tensor:latest
LABEL maintainer "Jimmy Lee"
WORKDIR /mnt
COPY --from=builder /src/dist/* .
RUN python -m easy_install ./*.egg
ENTRYPOINT ["python", "-m", "nuclei_discovery"]
