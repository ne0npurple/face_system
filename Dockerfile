FROM tensorflow:2.4.2-gpu

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "main.py" ]
