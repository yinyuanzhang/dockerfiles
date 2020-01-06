FROM jarppe/musl-tools:latest AS base


RUN echo "void main() {}" > true.c && \
    musl-gcc -static -o true true.c


FROM scratch AS done

COPY --from=base /true /true
CMD ["/true"]
