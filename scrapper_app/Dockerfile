# an app to scrap and create index.html with quote of the day
FROM frolvlad/alpine-python3
RUN mkdir /Data /Web
ADD scrapper.py /Data/
RUN pip install requests
ENTRYPOINT ["python3",  "/Data/scrapper.py"]
