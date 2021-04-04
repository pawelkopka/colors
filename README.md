# Colors
API that serve colors from provide json file.

## Requiements
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

## How to run tests
Tox instll dependency and run pytest and black 
```bash
tox
```

## Asummptions
- Use file to persitance data 
- File loaded as volume to container
- Use python 3.8
- Respone json
- Post with data
- Post can overwrite

## What can be improve
- use database instead file
- 