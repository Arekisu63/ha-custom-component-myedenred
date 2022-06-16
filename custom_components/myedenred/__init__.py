"""The my_edenred integration."""
from __future__ import annotations
import logging

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN

__version__ = "1.0.0"
_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[str] = ["sensor"]

async def async_setup(hass: HomeAssistant, config: ConfigType):
    # Return boolean to indicate that initialization was successful.
    _LOGGER.info("async_setup")
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up the component from a config entry."""
    _LOGGER.info("Entry data: %s", entry.data)
    _LOGGER.info("Entry options: %s", entry.options)
    _LOGGER.info("Entry unique ID: %s", entry.unique_id)

    hass.data.setdefault(DOMAIN, {})

    hass.config_entries.async_setup_platforms(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok    