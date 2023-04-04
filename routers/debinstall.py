from fastapi import APIRouter
from utils.script import CheckV_and_Install

router = APIRouter()

@router.get('/syftD')
def syftUpdateDeb():
    chSyft = CheckV_and_Install('https://github.com/anchore/syft','syft', 0)
    chSyft.run()
    return chSyft.m

@router.get('/grypeD')
def grypeUpdateDeb():
    chGrype = CheckV_and_Install('https://github.com/anchore/grype','grype', 1)
    chGrype.run()
    return chGrype.m