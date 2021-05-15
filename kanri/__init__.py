from configparser import ConfigParser
from pyrogram import Client
import logging, threading

FORMAT = "[KanRi] %(message)s"

KLOCAL = threading.local()

logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt="[%X]")
logging.getLogger("pyrogram").setLevel(logging.WARNING)

KLOCAL.LOGGER = logging.getLogger(__name__)

KLOCAL.LOGGER.info("Kanri is starting..........")

parser = ConfigParser()
parser.read("config.ini")

kanriconf = parser["kanriconf"]
KLOCAL.owner_id = kanriconf.getint("owner_id")
dev_users = kanriconf.get("dev_users")
KLOCAL.dev_users = list(map(int, dev_users))
operators = kanriconf.get("operators")
KLOCAL.operators = list(map(int, operators))
KLOCAL.postgres_url = kanriconf.get("postgres_url")
KLOCAL.CF_API_KEY = kanriconf.get("CF_API_KEY", None)

plugins = parser["plugins"]
include = plugins.get("include")
KLOCAL.LOAD = list(map(str, include))
exclude = plugins.get("exclude")
KLOCAL.NO_LOAD = list(map(str, exclude))

KLOCAL.client = Client(":memory:", config_file="config.ini")
