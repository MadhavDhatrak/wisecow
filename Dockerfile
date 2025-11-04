FROM debian:stable-slim

RUN apt-get update && \
    apt-get install -y cowsay fortune-mod netcat-openbsd dos2unix && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/games:${PATH}"

WORKDIR /app

COPY wisecow.sh /app/wisecow.sh

RUN dos2unix /app/wisecow.sh && \
    chmod +x /app/wisecow.sh

EXPOSE 4499

CMD ["./wisecow.sh"]

