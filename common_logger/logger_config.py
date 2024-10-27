import logging


def configure_logger(
    level=logging.INFO,
):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s,%(msecs)03d] - %(module)s - %(levelname)s: %(message)s.",
    )
