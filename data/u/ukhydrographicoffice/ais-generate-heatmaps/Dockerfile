FROM openjdk:8-jdk AS builder

WORKDIR ais-heatmap-mob
COPY ./ ./
RUN ./gradlew clean assemble

FROM openjdk:8-jre

WORKDIR /opt/generate-heatmap/
COPY --from=builder ./ais-heatmap-mob/build/libs/*-all.jar ./heatmaps-all.jar
RUN chmod +x ./heatmaps-all.jar
CMD java -jar /opt/generate-heatmap/heatmaps-all.jar \
    -o $OUTPUT_DIRECTORY \
    -p $OUTPUT_FILENAME_PREFIX \
    -r $RESOLUTION \
    -t $RESAMPLING_TIME_THRESHOLD \
    -d $RESAMPLING_DISTANCE_THRESHOLD \
    -y $YEAR \
    -m $MONTH
