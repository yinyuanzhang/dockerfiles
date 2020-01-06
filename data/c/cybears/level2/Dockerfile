# First stage
FROM python:3.7-alpine as base
WORKDIR /ctf/
RUN echo "Grabbing our flag..."  
COPY flag.txt ./
RUN cat flag.txt > empty.txt
RUN echo "[This is an empty flag that the recipient will return through customs]" > empty.txt
COPY *.py ./
RUN ./create_flag_maze.py && \
./hide_flag.py && \
rm hide_flag.py && \
rm flag.txt

# Second stage
# No layers from the original stage will be available
FROM python:3.7-alpine
WORKDIR /ctf/
RUN adduser -D ctf 
COPY --from=base /ctf /ctf
RUN chown -R root:ctf /ctf
USER ctf
CMD cat empty.txt
