FROM tensorflow/tensorflow:2.4.2-gpu

WORKDIR /app

COPY retinaface_tf2/requirements.txt ./

RUN pip3 install -r requirements.txt

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV DEBIAN_FRONTEND=noninteractive
RUN sed -i 's/archive\.ubuntu\.com/tw.archive.ubuntu.com/' /etc/apt/sources.list
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-opencv && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN mkdir -p static/uploads

VOLUME [ "/app/model", "/app/checkpoints" ]

CMD [ "python3", "main.py" ]
