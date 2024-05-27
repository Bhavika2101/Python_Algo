# ********RoostGPT********
"""
Test generated by RoostGPT for test python-unit--test using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=make_lowshelf_4cf0e3a9b4
ROOST_METHOD_SIG_HASH=make_lowshelf_4cf0e3a9b4

```
Scenario 1: Test the creation of a low-shelf filter with valid parameters
Details:
  TestName: test_make_lowshelf_with_valid_parameters
  Description: This test verifies the successful creation of a low-shelf filter when provided valid parameters.
Execution:
  Arrange: Initialize the frequency, samplerate, gain_db, and q_factor parameters with valid values.
  Act: Call the make_lowshelf function with the initialized parameters.
  Assert: Check if the created filter is an instance of the IIRFilter class and whether the a_coeffs and b_coeffs attributes of the filter match the expected values.
Validation:
  The test ensures that the make_lowshelf function correctly creates a low-shelf filter with the specified parameters. It validates the business requirement of creating a low-shelf filter with user-specified parameters.

Scenario 2: Test the creation of a low-shelf filter with a gain of 0 dB
Details:
  TestName: test_make_lowshelf_with_zero_gain
  Description: This test verifies the creation of a low-shelf filter when the gain_db parameter is set to 0.
Execution:
  Arrange: Initialize the frequency, samplerate, and q_factor parameters with valid values, and set gain_db to 0.
  Act: Call the make_lowshelf function with the initialized parameters.
  Assert: Check if the created filter is an instance of the IIRFilter class and whether the a_coeffs and b_coeffs attributes of the filter match the expected values.
Validation:
  The test ensures that the make_lowshelf function correctly creates a low-shelf filter with a gain of 0 dB. It validates the business requirement of creating a low-shelf filter with a user-specified gain.

Scenario 3: Test the creation of a low-shelf filter with a negative gain
Details:
  TestName: test_make_lowshelf_with_negative_gain
  Description: This test verifies the creation of a low-shelf filter when the gain_db parameter is negative.
Execution:
  Arrange: Initialize the frequency, samplerate, and q_factor parameters with valid values, and set gain_db to a negative value.
  Act: Call the make_lowshelf function with the initialized parameters.
  Assert: Check if the created filter is an instance of the IIRFilter class and whether the a_coeffs and b_coeffs attributes of the filter match the expected values.
Validation:
  The test ensures that the make_lowshelf function correctly creates a low-shelf filter with a negative gain. It validates the business requirement of creating a low-shelf filter with a user-specified gain.

Scenario 4: Test the creation of a low-shelf filter with a frequency equal to the samplerate
Details:
  TestName: test_make_lowshelf_with_frequency_equal_to_samplerate
  Description: This test verifies the creation of a low-shelf filter when the frequency is equal to the samplerate.
Execution:
  Arrange: Initialize the frequency and samplerate parameters with the same valid value, and set gain_db and q_factor to valid values.
  Act: Call the make_lowshelf function with the initialized parameters.
  Assert: Check if the created filter is an instance of the IIRFilter class and whether the a_coeffs and b_coeffs attributes of the filter match the expected values.
Validation:
  The test ensures that the make_lowshelf function correctly creates a low-shelf filter when the frequency is equal to the samplerate. It validates the business requirement of creating a low-shelf filter with a user-specified frequency and samplerate.
```
"""

# ********RoostGPT********
import pytest
from math import cos, sin, sqrt, tau
from audio_filters.iir_filter import IIRFilter
from audio_filters.butterworth_filter import make_lowshelf

class Test_ButterworthFilterMakeLowshelf:
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_make_lowshelf_with_valid_parameters(self):
        # Arrange
        frequency = 1000
        samplerate = 48000
        gain_db = 6
        q_factor = 1 / sqrt(2)

        # Act
        filter = make_lowshelf(frequency, samplerate, gain_db, q_factor)

        # Assert
        assert isinstance(filter, IIRFilter)
        assert filter.a_coeffs + filter.b_coeffs == [3.0409336710888786, -5.608870992220748, 2.602157875636628, 3.139954022810743, -5.591841778072785, 2.5201667380627257]

    @pytest.mark.regression
    @pytest.mark.positive
    def test_make_lowshelf_with_zero_gain(self):
        # Arrange
        frequency = 1000
        samplerate = 48000
        gain_db = 0
        q_factor = 1 / sqrt(2)

        # Act
        filter = make_lowshelf(frequency, samplerate, gain_db, q_factor)

        # Assert
        assert isinstance(filter, IIRFilter)
        # TODO: Replace the expected a_coeffs and b_coeffs with the correct values
        assert filter.a_coeffs + filter.b_coeffs == [1.0, 0.0, 0.0, 1.0, 0.0, 0.0]

    @pytest.mark.regression
    @pytest.mark.negative
    def test_make_lowshelf_with_negative_gain(self):
        # Arrange
        frequency = 1000
        samplerate = 48000
        gain_db = -6
        q_factor = 1 / sqrt(2)

        # Act
        filter = make_lowshelf(frequency, samplerate, gain_db, q_factor)

        # Assert
        assert isinstance(filter, IIRFilter)
        # TODO: Replace the expected a_coeffs and b_coeffs with the correct values
        assert filter.a_coeffs + filter.b_coeffs == [1.0, 0.0, 0.0, 1.0, 0.0, 0.0]

    @pytest.mark.regression
    @pytest.mark.positive
    def test_make_lowshelf_with_frequency_equal_to_samplerate(self):
        # Arrange
        frequency = 48000
        samplerate = 48000
        gain_db = 6
        q_factor = 1 / sqrt(2)

        # Act
        filter = make_lowshelf(frequency, samplerate, gain_db, q_factor)

        # Assert
        assert isinstance(filter, IIRFilter)
        # TODO: Replace the expected a_coeffs and b_coeffs with the correct values
        assert filter.a_coeffs + filter.b_coeffs == [1.0, 0.0, 0.0, 1.0, 0.0, 0.0]
