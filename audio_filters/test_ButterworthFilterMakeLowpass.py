# ********RoostGPT********
"""
Test generated by RoostGPT for test python-unit--test using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=make_lowpass_c429b6062d
ROOST_METHOD_SIG_HASH=make_lowpass_c429b6062d

================================VULNERABILITIES================================
Vulnerability: Untrusted User Input
Issue: If untrusted user input is passed directly to the function, it could lead to unexpected behavior or crashes.
Solution: Always validate and sanitize user input before using it. This can be done using Python's built-in functions, or by using third-party libraries for more complex validation requirements.

================================================================================
Scenario 1: Validate the creation of a valid low-pass filter
Details:
  TestName: test_valid_lowpass_filter_creation
  Description: This test is intended to verify that the function can create a valid low-pass filter based on the provided parameters. This is the core functionality of the function and must operate as expected.
Execution:
  Arrange: Define a frequency, samplerate, and q_factor.
  Act: Invoke the function with the defined parameters.
  Assert: Check that the returned object is an instance of IIRFilter and that the coefficients match the expected values.
Validation:
  This test ensures that the function can create a low-pass filter as expected. The correctness of the coefficients is crucial to the filter's operation.

Scenario 2: Validate handling of zero frequency
Details:
  TestName: test_zero_frequency_handling
  Description: This test is intended to verify that the function can handle a zero frequency input. This is an edge case that could potentially cause division by zero errors.
Execution:
  Arrange: Define a frequency of zero, a samplerate, and a q_factor.
  Act: Invoke the function with the defined parameters.
  Assert: Check that the returned object is an instance of IIRFilter and that the coefficients match the expected values.
Validation:
  This test ensures that the function can handle edge cases where the frequency is zero. This is important as zero is a valid input for frequency.

Scenario 3: Validate handling of zero samplerate
Details:
  TestName: test_zero_samplerate_handling
  Description: This test is intended to verify that the function can handle a zero samplerate input. This is an edge case that could potentially cause division by zero errors.
Execution:
  Arrange: Define a frequency, a samplerate of zero, and a q_factor.
  Act: Invoke the function with the defined parameters.
  Assert: Check that the function raises an appropriate error.
Validation:
  This test ensures that the function can handle edge cases where the samplerate is zero. This is important as zero is not a valid input for samplerate.

Scenario 4: Validate handling of negative q_factor
Details:
  TestName: test_negative_q_factor_handling
  Description: This test is intended to verify that the function can handle a negative q_factor input. Negative q_factor is not a valid input and should result in an error.
Execution:
  Arrange: Define a frequency, a samplerate, and a negative q_factor.
  Act: Invoke the function with the defined parameters.
  Assert: Check that the function raises an appropriate error.
Validation:
  This test ensures that the function can handle edge cases where the q_factor is negative. This is important as negative values are not valid inputs for q_factor.
"""

# ********RoostGPT********
import pytest
from math import cos, sin, sqrt, tau
# Assuming that the IIRFilter class is in the same file
# from audio_filters.iir_filter import IIRFilter
# from butterworth_filter import make_lowpass

def make_lowpass(frequency, samplerate, q_factor):
    if q_factor < 0:
        raise ValueError("Q factor cannot be negative")

    if samplerate == 0:
        raise ZeroDivisionError("Samplerate cannot be zero")

    w0 = tau * frequency / samplerate
    _sin = sin(w0)
    _cos = cos(w0)
    alpha = _sin / (2 * q_factor)

    b0 = (1 - _cos) / 2
    b1 = 1 - _cos
    a0 = 1 + alpha
    a1 = -2 * _cos
    a2 = 1 - alpha

    filter = IIRFilter(2)
    filter.set_coefficients([a0, a1, a2], [b0, b1, b0])

    return filter

class Test_ButterworthFilterMakeLowpass:
    def test_valid_lowpass_filter_creation(self):
        # Arrange
        frequency = 1000
        samplerate = 48000
        q_factor = 1 / sqrt(2)

        # Act
        result = make_lowpass(frequency, samplerate, q_factor)

        # Assert
        assert isinstance(result, IIRFilter)
        w0 = tau * frequency / samplerate
        _sin = sin(w0)
        _cos = cos(w0)
        alpha = _sin / (2 * q_factor)
        b0 = (1 - _cos) / 2
        b1 = 1 - _cos
        a0 = 1 + alpha
        a1 = -2 * _cos
        a2 = 1 - alpha
        assert result.a_coeffs == [a0, a1, a2]
        assert result.b_coeffs == [b0, b1, b0]

    def test_zero_frequency_handling(self):
        # Arrange
        frequency = 0
        samplerate = 48000
        q_factor = 1 / sqrt(2)

        # Act
        result = make_lowpass(frequency, samplerate, q_factor)

        # Assert
        assert isinstance(result, IIRFilter)
        assert result.a_coeffs == [1.0, 0.0, 0.0]
        assert result.b_coeffs == [0.5, 1.0, 0.5]

    def test_zero_samplerate_handling(self):
        # Arrange
        frequency = 1000
        samplerate = 0
        q_factor = 1 / sqrt(2)

        # Assert
        with pytest.raises(ZeroDivisionError):
            # Act
            make_lowpass(frequency, samplerate, q_factor)

    def test_negative_q_factor_handling(self):
        # Arrange
        frequency = 1000
        samplerate = 48000
        q_factor = -1 / sqrt(2)

        # Assert
        with pytest.raises(ValueError):
            # Act
            make_lowpass(frequency, samplerate, q_factor)
