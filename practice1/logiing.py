from logging import StreamHandler, getLogger,DEBUG
logger=getLogger(__name__)
handler=StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.debug('これはデバッグログです')
