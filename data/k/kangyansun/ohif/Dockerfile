FROM ubuntu:16.04
MAINTAINER Raphael Erard (raphael.erard@adis-sa.ch)
RUN apt-get update && apt-get install -y nodejs-legacy npm curl git
RUN curl "https://install.meteor.com/?release=1.6" | sh
WORKDIR /opt
RUN mkdir ohif
RUN git clone https://github.com/OHIF/Viewers
WORKDIR /opt/Viewers
RUN git checkout -b master-docker 004ccbc
WORKDIR /opt/Viewers/OHIFViewer
RUN npm install --production
ENV METEOR_PACKAGE_DIRS="/opt/Viewers/Packages/"
ENV METEOR_SETTINGS="{\"servers\":{\"dicomWeb\":[{\"name\":\"Orthanc\",\"wadoUriRoot\":\"http://ohif:8042/wado\",\"qidoRoot\": \"http://ohif:8042/dicom-web\",\"wadoRoot\": \"http://ohif:8042/dicom-web\",\"qidoSupportsIncludeField\": false,\"imageRendering\": \"wadouri\",\"thumbnailRendering\": \"wadors\",\"requestOptions\": {  \"auth\": \"orthanc:orthanc\",\"logRequests\": true,\"logResponses\": false,\"logTiming\": true}}]},\"defaultServiceType\": \"dicomWeb\",\"dropCollections\": true,\"public\":{\"verifyEmail\": false,\"ui\":{\"studyListFunctionsEnabled\": true,\"leftSidebarOpen\": false,\"displaySetNavigationLoopOverSeries\": false,\"displaySetNavigationMultipleViewports\": true,\"autoPositionMeasurementsTextCallOuts\": \"TRLB\"}},\"proxy\":{\"enabled\": true}}"
RUN echo $METEOR_SETTINGS
RUN meteor build --directory /opt/ohif/ --allow-superuser
WORKDIR /opt/ohif/bundle/programs/server
RUN npm install
ENV MONGO_URL=mongodb://mongodb:27017/myapp
ENV ROOT_URL=http://localhost:3000
ENV PORT=3000
WORKDIR /opt/ohif/bundle
CMD meteor node main.js
