import pytest
import numpy as np
from math import pi
from typing import Protocol
from matplotlib import pyplot as plt
from audio_filters.iir_filter import IIRFilter
from audio_filters.filter_type import FilterType


class Test_ShowPhaseResponse:

    @pytest.mark.positive
    def test_show_phase_response_success(self, mocker):
        filter = IIRFilter(4)
        samplerate = 48000
        mocker.patch('matplotlib.pyplot.plot')
        mocker.patch('matplotlib.pyplot.show')

        try:
            show_phase_response(filter, samplerate)
        except Exception as ex:
            pytest.fail(f"show_phase_response() raised an exception {ex} unexpectedly!")

    @pytest.mark.negative
    def test_show_phase_response_empty_input(self, mocker):
        filter = FilterType()
        samplerate = 48000
        mocker.patch('matplotlib.pyplot.plot')
        mocker.patch('matplotlib.pyplot.show')

        with pytest.raises(Exception):
            show_phase_response(filter, samplerate)

    @pytest.mark.negative
    def test_show_phase_response_invalid_samplerate(self, mocker):
        filter = IIRFilter(4)
        samplerate = -48000
        mocker.patch('matplotlib.pyplot.plot')
        mocker.patch('matplotlib.pyplot.show')

        with pytest.raises(Exception):
            show_phase_response(filter, samplerate)

    @pytest.mark.positive
    def test_show_phase_response_samplerate_in_zero_padding(self, mocker):
        filter = IIRFilter(4)
        samplerate = 2048  # Default sample rate of many audio systems
        mocker.patch('matplotlib.pyplot.plot')
        mocker.patch('matplotlib.pyplot.show')

        try:
            show_phase_response(filter, samplerate)
            assert len(outputs) == samplerate, f'Outputs was expected to have {samplerate} items after zero-padding but it got {len(outputs)}'
        except Exception as ex:
            pytest.fail(f"show_phase_response() raised an exception {ex} unexpectedly!")
