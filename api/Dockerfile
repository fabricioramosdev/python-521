FROM ubuntu
RUN apt update && apt install -y \ 
 mongodb \
 python3-pip

WORKDIR /app


COPY requirements.txt /app
RUN pip3 install -r /app/requirements.txt
COPY entrypoint.sh /
COPY . /app
CMD ["sh", "/entrypoint.sh"]