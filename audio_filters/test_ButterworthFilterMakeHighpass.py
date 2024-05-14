# ********RoostGPT********
"""
Test generated by RoostGPT for test python-unit--test using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=make_highpass_82938f5d7d
ROOST_METHOD_SIG_HASH=make_highpass_82938f5d7d

Scenario 1: Validate the creation of a high-pass filter with default q_factor
Details:
  TestName: test_make_highpass_default_q_factor
  Description: This test will verify if the make_highpass function creates an IIRFilter object with the correct coefficients when the q_factor is not explicitly specified (default value is used).
Execution:
  Arrange: Initialize frequency and samplerate values.
  Act: Call the make_highpass function with frequency and samplerate as parameters.
  Assert: Check if the returned IIRFilter object has the correct coefficients.
Validation:
  This test validates the default behavior of the make_highpass function. It ensures that the function can correctly produce a high-pass filter with the default q_factor.

Scenario 2: Validate the creation of a high-pass filter with a specific q_factor
Details:
  TestName: test_make_highpass_specific_q_factor
  Description: This test will verify if the make_highpass function creates an IIRFilter object with the correct coefficients when a specific q_factor is provided.
Execution:
  Arrange: Initialize frequency, samplerate, and q_factor values.
  Act: Call the make_highpass function with frequency, samplerate, and q_factor as parameters.
  Assert: Check if the returned IIRFilter object has the correct coefficients.
Validation:
  This test validates the make_highpass function's ability to correctly produce a high-pass filter with a specific q_factor. It ensures the function's flexibility and adherence to the provided filter specifications.

Scenario 3: Validate the behavior of the function with zero frequency
Details:
  TestName: test_make_highpass_zero_frequency
  Description: This test will verify the behavior of the make_highpass function when the frequency is zero.
Execution:
  Arrange: Initialize frequency as zero and provide a valid samplerate value.
  Act: Call the make_highpass function with the frequency and samplerate as parameters.
  Assert: Check the returned IIRFilter object's coefficients.
Validation:
  This test verifies the function's ability to handle edge cases, specifically when the frequency is zero. The expected coefficients in this case are important to validate the function's correct implementation.

Scenario 4: Validate the behavior of the function with maximum frequency
Details:
  TestName: test_make_highpass_max_frequency
  Description: This test will verify the behavior of the make_highpass function when the frequency is at maximum (equal to the samplerate).
Execution:
  Arrange: Initialize frequency equal to the samplerate.
  Act: Call the make_highpass function with the frequency and samplerate as parameters.
  Assert: Check the returned IIRFilter object's coefficients.
Validation:
  This test checks the function's ability to handle edge cases, specifically when the frequency is at its maximum possible value (equal to the samplerate). The expected coefficients in this case are important to validate the function's correct implementation.
"""

# ********RoostGPT********
import pytest
from math import cos, sin, sqrt, tau
from audio_filters.iir_filter import IIRFilter
from butterworth_filter import make_highpass


class Test_ButterworthFilterMakeHighpass:
    
    @pytest.mark.regression
    def test_make_highpass_default_q_factor(self):
        # Arrange
        frequency = 1000
        samplerate = 48000
        q_factor = 1 / sqrt(2)
        w0 = tau * frequency / samplerate
        _sin = sin(w0)
        _cos = cos(w0)
        alpha = _sin / (2 * q_factor)
        b0 = (1 + _cos) / 2
        b1 = -1 - _cos
        a0 = 1 + alpha
        a1 = -2 * _cos
        a2 = 1 - alpha
        expected_coeffs = [a0, a1, a2, b0, b1, b0]

        # Act
        filter = make_highpass(frequency, samplerate)

        # Assert
        assert filter.a_coeffs + filter.b_coeffs == pytest.approx(expected_coeffs)

    @pytest.mark.regression
    def test_make_highpass_specific_q_factor(self):
        # Arrange
        frequency = 1000
        samplerate = 48000
        q_factor = 0.7
        w0 = tau * frequency / samplerate
        _sin = sin(w0)
        _cos = cos(w0)
        alpha = _sin / (2 * q_factor)
        b0 = (1 + _cos) / 2
        b1 = -1 - _cos
        a0 = 1 + alpha
        a1 = -2 * _cos
        a2 = 1 - alpha
        expected_coeffs = [a0, a1, a2, b0, b1, b0]

        # Act
        filter = make_highpass(frequency, samplerate, q_factor)

        # Assert
        assert filter.a_coeffs + filter.b_coeffs == pytest.approx(expected_coeffs)

    @pytest.mark.edge
    def test_make_highpass_zero_frequency(self):
        # Arrange
        frequency = 0
        samplerate = 48000
        q_factor = 1 / sqrt(2)
        w0 = tau * frequency / samplerate
        _sin = sin(w0)
        _cos = cos(w0)
        alpha = _sin / (2 * q_factor)
        b0 = (1 + _cos) / 2
        b1 = -1 - _cos
        a0 = 1 + alpha
        a1 = -2 * _cos
        a2 = 1 - alpha
        expected_coeffs = [a0, a1, a2, b0, b1, b0]

        # Act
        filter = make_highpass(frequency, samplerate)

        # Assert
        assert filter.a_coeffs + filter.b_coeffs == pytest.approx(expected_coeffs)

    @pytest.mark.edge
    def test_make_highpass_max_frequency(self):
        # Arrange
        samplerate = 48000
        frequency = samplerate
        q_factor = 1 / sqrt(2)
        w0 = tau * frequency / samplerate
        _sin = sin(w0)
        _cos = cos(w0)
        alpha = _sin / (2 * q_factor)
        b0 = (1 + _cos) / 2
        b1 = -1 - _cos
        a0 = 1 + alpha
        a1 = -2 * _cos
        a2 = 1 - alpha
        expected_coeffs = [a0, a1, a2, b0, b1, b0]

        # Act
        filter = make_highpass(frequency, samplerate)

        # Assert
        assert filter.a_coeffs + filter.b_coeffs == pytest.approx(expected_coeffs)
