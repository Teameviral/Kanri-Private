from pyrogram.session import Session
from pyrogram import __version__, idle
from kanri import KLOCAL
import asyncio, logging, os, importlib


async def load():
    if os.name != 'nt':
        path = 'kanri/plugins'
    else:
        path = 'kanri\plugins'

    for x in os.listdir(path):
        if hasattr(x, 'name'):
            KLOCAL.LOGGER.info(f'[LOADER] Found path {x.name}')
        try:
            for y in os.listdir(x):
                if hasattr(y, 'name'):
                    if y.name.endswith('.py'):
                        importlib.import_module(name=y, package=x)
                        KLOCAL.LOGGER.info(f'[LOADER] Loading {y.name} from package {x.name}')
        except BaseException:
            pass


async def run_kanri():
    '''
    Kanri's asynchronous entry point, all startup events are initalised here.
    '''
    try:
        await load()
        KLOCAL.LOGGER.info("Starting Kanri's Pyrogram Client")
        await KLOCAL.client.start()
        KLOCAL.LOGGER.info("Kanri started!")
        await idle()
    except BaseException as error:
        KLOCAL.LOGGER.exception(f"Exiting due to a {type(error).__name__}: {error}")
    finally:
        KLOCAL.LOGGER.warning("Kanri is shutting down")


if __name__ == "__main__":
    KLOCAL.LOGGER.info(
        f"""Starting Kanri, powered by Pyrogram (v{__version__}). Copyright (C) 2021 Intellivoid Technologies
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions, check the LICENSE file for more information."""
    )
    KLOCAL.LOGGER.info("Initializing Kanri")
    # Sets pyrogram logging to warning because info is too verbose
    KLOCAL.LOGGER.info("Setting pyrogram logs to warning to avoid verbose output and disabling the session notice")
    logging.getLogger("pyrogram").setLevel(logging.WARNING)
    Session.notice_displayed = True
    KLOCAL.LOGGER.info("Starting asyncio event loop")
    asyncio.get_event_loop().run_until_complete(run_kanri())
