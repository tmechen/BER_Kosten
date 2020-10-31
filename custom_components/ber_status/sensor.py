"""Platform for sensor integration."""
from homeassistant.helpers.entity import Entity


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    add_entities([BERStatus()])


class BERStatus(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = True

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'BER Status'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state
