FROM python

WORKDIR /glowmarkt

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY src/ .
EXPOSE 5000
CMD ["python3", "./app.py"]