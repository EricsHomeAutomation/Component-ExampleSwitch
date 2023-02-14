import logging

from homeassistant.components.switch import (PLATFORM_SCHEMA, SwitchEntity)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from homeassistant.const import STATE_ON

from homeassistant.const import CONF_NAME, CONF_IP_ADDRESS

import homeassistant.helpers.config_validation as cv

import voluptuous as vol

_LOGGER = logging.getLogger(__name__)


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME): cv.string,
    vol.Required(CONF_IP_ADDRESS): cv.string,
})

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None:
    name = config[CONF_NAME]
    ip = config[CONF_IP_ADDRESS]
    add_entities([ExampleSwitchEntity(name, ip)])


class ExampleSwitchEntity(SwitchEntity):
    """Representation of Switch Sensor."""

    def __init__(self, name, ip):
        """Initialize the sensor."""
        self._pre = "sw_"
        self._name = name
        self._state = False

    @property
    def is_on(self):
        """Return is_on status."""
        return self._state

    async def async_turn_on(self):
        """Turn On method."""
        _LOGGER.warning("Async switch turned on")
        self._state = True
        self.schedule_update_ha_state()

    async def async_turn_off(self):
        """Turn Off method."""
        _LOGGER.warning("Example switch turned off")
        self._state = False
        self.schedule_update_ha_state()

    # @property
    # def should_poll(self):
    #     """No polling needed."""
    #     return False

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    # @property
    # def available(self):
    #     """Return availability."""
    #     return True

    async def async_update(self):
        """Return sensor state."""
        return False
