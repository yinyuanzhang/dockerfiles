FROM alpine

COPY ./IntelliJIDEALicenseServer_linux_amd64 ./IntelliJIDEALicenseServer_linux_amd64
COPY ./IntelliJIDEALicenseServer.html ./IntelliJIDEALicenseServer.html
RUN chmod +x ./IntelliJIDEALicenseServer_linux_amd64
EXPOSE 80

CMD ["./IntelliJIDEALicenseServer_linux_amd64", "-p", "80"]