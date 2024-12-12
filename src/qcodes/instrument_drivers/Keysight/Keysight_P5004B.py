from typing import TYPE_CHECKING

from . import N52xx

if TYPE_CHECKING:
    from typing_extensions import Unpack

    from qcodes.instrument import VisaInstrumentKWArgs


class KeysightP5004B(N52xx.KeysightPNAxBase):
    def __init__(
        self, name: str, address: str, **kwargs: "Unpack[VisaInstrumentKWArgs]"
    ):
        super().__init__(
            name,
            address,
            min_freq=9e3, #Min 1 KHz
            max_freq=20e9, #Max 20 GHz
            min_power=-80, #Min power
            max_power=10, #Max power
            nports=2, #Number of ports
            **kwargs,
        )

        attenuators_options = {"219", "419"}
        options = set(self.get_options())
        if attenuators_options.intersection(options):
            self._set_power_limits(min_power=-100, max_power=10) #-80 dBm - 20 dBm power attenuator.
        if "080" in options:
            self._enable_fom()
