FROM python:3.6

COPY /static-routing /home/static-routing

WORKDIR /home/static-routing

RUN pip install -r requirements.txt

ENTRYPOINT ["python3.6"]

CMD ["static-routing.py"]
