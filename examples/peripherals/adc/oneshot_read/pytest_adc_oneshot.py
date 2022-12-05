# SPDX-FileCopyrightText: 2021-2022 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: CC0-1.0

import pytest
from pytest_embedded.dut import Dut


@pytest.mark.esp32
@pytest.mark.esp32s2
@pytest.mark.esp32s3
@pytest.mark.esp32c3
@pytest.mark.esp32c6
@pytest.mark.adc
def test_adc_oneshot(dut: Dut) -> None:
    dut.expect(r'EXAMPLE: ADC1 Channel\[(\d+)\] Raw Data: (\d+)', timeout=5)


@pytest.mark.esp32c2
@pytest.mark.adc
@pytest.mark.xtal_26mhz
@pytest.mark.parametrize(
    'config, baud',
    [
        ('esp32c2_xtal26m', '74880'),
    ],
    indirect=True,
)
def test_adc_oneshot_esp32c2_xtal_26mhz(dut: Dut) -> None:
    dut.expect(r'EXAMPLE: ADC1 Channel\[(\d+)\] Raw Data: (\d+)', timeout=5)
