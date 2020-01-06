FROM alpine:3.5
WORKDIR /jetbrains
ADD ./IntelliJIDEALicenseServer_linux_amd64 .
RUN chmod +x ./IntelliJIDEALicenseServer_linux_amd64
EXPOSE 1027
CMD ["./IntelliJIDEALicenseServer_linux_amd64"]
