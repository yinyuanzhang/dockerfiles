FROM python:3.7-alpine as base

LABEL bio_node=v1.0 \
      bionode_entrypoint="python -m mifaser.bionode" \
      input_1="fasta_file|fasta_gz|fastq_file|fastq_gz|url|sra_id" \
      input_2="fasta_file|fasta_gz|fastq_file|fastq_gz|url|sra_id" \
      output="mifaser_out" \
      maintainer="mmiller@bromberglab.org" \
      description="mi-faser docker image (https://services.bromberglab.org/mifaser)"

FROM base as builder

# setup system
RUN mkdir /install
WORKDIR /install
# RUN apk update && apk add git && rm -rf /var/cache/apk/*

# setup app
COPY . /app
# RUN pip install --upgrade pip && pip install --prefix=/install -r /app/requirements.txt
# RUN (chmod a+x /app/setup.sh; /app/setup.sh)

FROM base

COPY --from=builder /install /usr/local
COPY --from=builder /app /app

# set environment variables
WORKDIR /app
ENV INPUT_PATH=/input OUTPUT_PATH=/output 

# set app ENTRYPOINT
ENTRYPOINT ["python", "-m", "mifaser.cli"]

# set app CMD
CMD ["--version"]
