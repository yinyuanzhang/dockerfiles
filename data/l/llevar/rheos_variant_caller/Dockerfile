FROM python:3.7.2-alpine3.8
#FROM snp_caller_test:temp
RUN apk add --no-cache build-base python3-dev zlib-dev cython make bzip2-dev xz-dev libcurl
WORKDIR /app
COPY . /app/
RUN python setup.py install
RUN mkdir /app/log && touch /app/log/variant_caller.log
ENTRYPOINT ["python", "variant_caller/get_variant_calls.py"]
#CMD ["file", \
#"-i", "/Users/siakhnin/data/giab/RMNISTHS_30xdownsample_50000000-63025520.name_sorted.fastq", \
#"-r", "/Users/siakhnin/data/reference/genome.mmi", \
#"-g", "20:50000000-63025520", \
#"-k", "localhost:9092", \
#"--bin_size=10000", \
#"--num_bins=100", \
#"--check_freq=1000"]
