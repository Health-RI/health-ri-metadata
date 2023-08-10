# Preprocess dcat-ap-3.0.0 shapes

## Rationale
The DCAT-AP 3.0.0 shapes are structured in a way that does not work with the current FDP client (v1.17.0). A workaround to have this function in the FDP client is to merge the SHACL constraints by grouping them based on the `sh:path`.

## Setup
```sh
python3 -m pip install -r requirements.txt
```

## Run
```sh
python3 ./preprocess.py
```
