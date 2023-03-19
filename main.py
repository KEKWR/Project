from fastapi import FastAPI
from script import CheckV_and_Install

app =FastAPI()

@app.get('/syftD')
def syftUpdateDeb():
    chSyft = CheckV_and_Install('https://github.com/anchore/syft','syft', 0)
    chSyft.run()
    return chSyft.m

@app.get('/grypeD')
def grypeUpdateDeb():
    chGrype = CheckV_and_Install('https://github.com/anchore/grype','grype', 1)
    chGrype.run()
    return chGrype.m
