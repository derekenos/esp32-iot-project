"""Additionality functionality to complement the MicroPython machine module.
"""

from machine import Timer as _Timer


class Timer(_Timer):
    """Augment Timer with methods for dynamic timer allocation.
    """

    # Assume that 4 hardware timers are available with no virtual timer
    # support, which is the case for the ESP32.
    available_timers = [
        _Timer(0),
        _Timer(1),
        _Timer(2),
        _Timer(3),
    ]

    @classmethod
    def allocate(cls):
        if len(cls.available_timers) == 0:
            raise RuntimeError('No available timers')
        return cls.available_timers.pop()

    @classmethod
    def deallocate(cls, timer):
        cls.available_timers.append(timer)
