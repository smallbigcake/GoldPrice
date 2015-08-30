
import logging

logger = logging.getLogger("GoldPrice")
logger.setLevel(logging.DEBUG)
logFile = logging.FileHandler("gold.log")
logScreen = logging.StreamHandler()
formatter = logging.Formatter("[%(asctime)s][%(name)s] %(levelname)s: %(message)s")

logFile.setFormatter(formatter)
logScreen.setFormatter(formatter)
logger.addHandler(logFile)
logger.addHandler(logScreen)


