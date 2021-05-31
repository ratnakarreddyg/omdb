FROM python:3.8-slim
RUN pip install requests
ADD movie.py /
ENTRYPOINT [ "python", "./movie.py" ]
