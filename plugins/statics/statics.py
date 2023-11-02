import logging

from pelican import signals

log = logging.getLogger(__name__)


def test(sender):
    log.debug("%s initialized !!", sender)


def register():
    signals.initialized.connect(test)
