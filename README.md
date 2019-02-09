# dojo_web
a simple contained app to scrap and get 1 random quote of the day from
http://dojodevopschallenge.s3-website-eu-west-1.amazonaws.com/fortune_of_the_day.json

everyday and display it in a containerized web app.


to use
* build docker image

```
cd scrapper_app
docker build .
```

* replace image name in kubernetes yaml file

* run kubernetes stack

```
 kubectl apply -f quote_of_the_day.yaml
```
