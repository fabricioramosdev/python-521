
FROM ubuntu
RUN apt update && apt install vim apache2 -y
COPY entrypoint.sh /
CMD ["sh", "/entrypoint.sh"]

