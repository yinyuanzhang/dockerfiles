FROM alpine:3.5
COPY ping /

HEALTHCHECK --interval=5s --timeout=3s \
    CMD ps aux | grep '[s]h ping' || exit 1
    
CMD ["sh", "ping"]
