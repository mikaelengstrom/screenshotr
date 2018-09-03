# Screenshotr

A Prototype of a website-screenshots SAAS.


## Requirements
- [Docker](https://docs.docker.com/install/)

## Install project locally 
- Clone repo
- `cd screenshotr`
- `docker-compose up`

Only tested on osx.

## The basic idea


Do a request of URL´s like this:
`POST /api/jobs/`

```json
{
  "urls": [
    "https://example.com",
    "https://asdf.com",
    "https://stallman.org",
    "https://news.ycombinator.com/"
  ]
}
```

And receive a response like this:
```json
{
  "uuid":"49dc5eec-5df3-4ed6-a48f-04f95ec1a49e",
  "created":"2018-09-03T20:34:51.147625Z",
  "status":"Finished",
  "job_url":"/api/jobs/49dc5eec-5df3-4ed6-a48f-04f95ec1a49e/",
  "urls": [
    {
      "url":"https://example.com",
      "image":"/media/httpsexamplecom-2018-09-03-2034511917630000.jpg",
    },{
      "url":"https://asdf.com",
      "image":"/media/httpsasdfcom-2018-09-03-2034511923250000.jpg",
    },{
      "url":"https://stallman.org",
      "image":"/media/httpsstallmanorg-2018-09-03-2034511929130000.jpg",
    },
    { 
      "url":"https://news.ycombinator.com/",
      "image":"/media/httpsnewsycombinatorcom-2018-09-03-2034511985450000.jpg",
    }
  ]
}
```

... or just browse to [http://localhost:8000/api/jobs/](http://localhost:8000/api/jobs/) and fiddle in [DRF](http://www.django-rest-framework.org/)-debugger.


Happy crawling!

