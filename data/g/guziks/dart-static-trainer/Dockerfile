FROM google/dart:1
ONBUILD WORKDIR /app
ONBUILD COPY --from=builder /app/main.snap ./
ONBUILD RUN dart \
    --snapshot=main.snap \
    --snapshot-kind=app-jit \
    main.snap train
