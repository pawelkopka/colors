# Colors
API that serves colors from provided json file.

## Requirements
- podman
- tox
- curl

## How to run
Build image
```bash
podman build . --tag colors:v0.1.0
```

Run App
```bash
podman run --rm -p 5000:5000 -v /home/kepok/redhat/colors/colors.json:/colors/cols.json:rw colors:v0.1.0 --name colors
```

Open browsers or curl http://localhost:5000/colors

## How to use
Get full colors list
```bash
curl http://localhost:5000/colors
```
Get color
```bash
curl http://localhost:5000/blue
```
Post color
```bash
curl -X POST http://localhost:5000/pink -d "#FFC0CB"
```

with ## How to run tests
Tox install dependency and run pytest and black 
```bash
tox
```

## Assumptions
- Use file to persistence data 
- File loaded as volume to a container
- Use python 3.8
- Response  with json
- Post with data
- Post can overwrite

## What can be improved
- use database instead of file