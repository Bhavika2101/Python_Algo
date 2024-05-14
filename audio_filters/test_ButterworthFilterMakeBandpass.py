# ********RoostGPT********
"""
Test generated by RoostGPT for test python-unit--test using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=make_bandpass_e90e9eadc4
ROOST_METHOD_SIG_HASH=make_bandpass_e90e9eadc4

Scenario 1: Test to validate the creation of the band-pass filter with valid input parameters
Details:
  TestName: test_make_bandpass_valid_input
  Description: This test is intended to verify the creation of the band-pass filter with valid input parameters.
Execution:
  Arrange: Initialize frequency, samplerate, and q_factor with valid values.
  Act: Invoke the make_bandpass function with the initialized parameters.
  Assert: Check if the created filter's a_coeffs and b_coeffs match the expected values.
Validation:
  This test is essential to ensure that the function works as expected with valid input parameters and creates the correct band-pass filter.

Scenario 2: Test to validate the creation of the band-pass filter with default q_factor
Details:
  TestName: test_make_bandpass_default_q_factor
  Description: This test is intended to verify the creation of the band-pass filter with the default q_factor.
Execution:
  Arrange: Initialize frequency and samplerate with valid values.
  Act: Invoke the make_bandpass function with the initialized parameters and the default q_factor.
  Assert: Check if the created filter's a_coeffs and b_coeffs match the expected values.
Validation:
  This test is vital to ensure that the function can create the correct band-pass filter using the default q_factor.

Scenario 3: Test to validate the creation of the band-pass filter with frequency equal to zero
Details:
  TestName: test_make_bandpass_zero_frequency
  Description: This test is intended to verify the creation of the band-pass filter with zero frequency.
Execution:
  Arrange: Initialize frequency with zero, and samplerate and q_factor with valid values.
  Act: Invoke the make_bandpass function with the initialized parameters.
  Assert: Check if the created filter's a_coeffs and b_coeffs match the expected values.
Validation:
  This test is significant to ensure that the function can handle the edge case where the frequency is zero and still create the correct band-pass filter.

Scenario 4: Test to validate the creation of the band-pass filter with samplerate equal to zero
Details:
  TestName: test_make_bandpass_zero_samplerate
  Description: This test is intended to verify if the division by zero error is raised when the samplerate is zero.
Execution:
  Arrange: Initialize samplerate with zero, and frequency and q_factor with valid values.
  Act: Invoke the make_bandpass function with the initialized parameters.
  Assert: Check if the division by zero error is raised.
Validation:
  This test is critical to ensure that the function handles the division by zero error correctly when the samplerate is zero. 

Scenario 5: Test to validate the creation of the band-pass filter with q_factor equal to zero
Details:
  TestName: test_make_bandpass_zero_q_factor
  Description: This test is intended to verify if the division by zero error is raised when the q_factor is zero.
Execution:
  Arrange: Initialize q_factor with zero, and frequency and samplerate with valid values.
  Act: Invoke the make_bandpass function with the initialized parameters.
  Assert: Check if the division by zero error is raised.
Validation:
  This test is crucial to ensure that the function handles the division by zero error correctly when the q_factor is zero.
"""

# ********RoostGPT********
import pytest
from math import sqrt
from audio_filters.iir_filter import IIRFilter
from butterworth_filter import make_bandpass

class Test_ButterworthFilterMakeBandpass:

    @pytest.mark.positive
    def test_make_bandpass_valid_input(self):
        frequency = 1000
        samplerate = 48000
        q_factor = 1 / sqrt(2)
        expected_a_coeffs = [1.0922959556412573, -1.9828897227476208, 0.9077040443587427]
        expected_b_coeffs = [0.06526309611002579, 0, -0.06526309611002579]
        filter = make_bandpass(frequency, samplerate, q_factor)
        assert filter.a_coeffs == expected_a_coeffs
        assert filter.b_coeffs == expected_b_coeffs

    @pytest.mark.positive
    def test_make_bandpass_default_q_factor(self):
        frequency = 1000
        samplerate = 48000
        expected_a_coeffs = [1.0922959556412573, -1.9828897227476208, 0.9077040443587427]
        expected_b_coeffs = [0.06526309611002579, 0, -0.06526309611002579]
        filter = make_bandpass(frequency, samplerate)
        assert filter.a_coeffs == expected_a_coeffs
        assert filter.b_coeffs == expected_b_coeffs

    @pytest.mark.negative
    def test_make_bandpass_zero_frequency(self):
        frequency = 0
        samplerate = 48000
        q_factor = 1 / sqrt(2)
        expected_a_coeffs = [1.0, 0.0, 0.0]
        expected_b_coeffs = [0.0, 0.0, 0.0]
        filter = make_bandpass(frequency, samplerate, q_factor)
        assert filter.a_coeffs == expected_a_coeffs
        assert filter.b_coeffs == expected_b_coeffs

    @pytest.mark.negative
    def test_make_bandpass_zero_samplerate(self):
        frequency = 1000
        samplerate = 0
        q_factor = 1 / sqrt(2)
        with pytest.raises(ZeroDivisionError):
            make_bandpass(frequency, samplerate, q_factor)

    @pytest.mark.negative
    def test_make_bandpass_zero_q_factor(self):
        frequency = 1000
        samplerate = 48000
        q_factor = 0
        with pytest.raises(ZeroDivisionError):
            make_bandpass(frequency, samplerate, q_factor)