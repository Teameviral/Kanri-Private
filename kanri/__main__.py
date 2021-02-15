from pyrogram import idle
from kanri import kanri, LOGGER


if __name__ == "__main__":
    kanri.start()
    LOGGER.info("Kanri started!")
    idle()

