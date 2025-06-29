import scrython
import scrython.cards
import time
class ScrythonApi:
    def getCardInfo(name):
        time.sleep(0.1)
        return scrython.cards.Named(exact=name)
    def getCardAlternateArtInfo(code, collectorNumber):
        time.sleep(0.1)
        return scrython.cards.Collector(code=code, collector_number=collectorNumber)
