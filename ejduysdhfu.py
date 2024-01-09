#логування - вивід помилок через бібліотеку
import logging
#запис у файл
logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w")
logging.debug("debug")
logging.info("Інформація про рядок коду")