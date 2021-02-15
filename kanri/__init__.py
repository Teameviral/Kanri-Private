from configparser import ConfigParser
from pyrogram import Client
import logging

FORMAT = "%(message)s"

logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt="[%X]")
logging.getLogger("pyrogram").setLevel(logging.WARNING)

LOGGER = logging.getLogger(__name__)

LOGGER.info("Kanri is starting..........")

parser = ConfigParser()
parser.read("config.ini")

kanriconf = parser["kanriconf"]
owner_id = kanriconf.getint("owner_id")
dev_users = kanriconf.get("dev_users")
dev_users = list(map(int, dev_users))
operators = kanriconf.get("operators")
operators = list(map(int, operators))
postgres_url = kanriconf.get("postgres_url")
CF_API_KEY = kanriconf.get("CF_API_KEY", None)

plugins = parser["plugins"]
include = plugins.get("include")
LOAD = list(map(str, include))
exclude = plugins.get("exclude")
NO_LOAD = list(map(str, exclude))

kanri = Client(":memory:", config_file="config.ini")
