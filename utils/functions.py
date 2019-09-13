import json
import logging


def loadConfigFile():
    logging.info("LOAD PARAMS FILE")
    with open("./params.json") as f_obj:
        return json.loads(f_obj.read())
