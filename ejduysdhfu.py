#логування - вивід помилок через бібліотеку
import logging
#запис у файл
logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode = "w")
logging.debug("debug")
logging.info("Інформація про рядок коду")
logging.warning("Попередження про можливу помилку")
logging.error("Помилка в програмі")
logging.critical("Критична помилка")

try:
    print(10/0)
except Exception:
    logging.exception("Exeption")