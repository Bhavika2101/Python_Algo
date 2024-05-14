# ********RoostGPT********
"""
Test generated by RoostGPT for test python-algo using AI Type Azure Open AI and AI Model roostgpt-4-32k

ROOST_METHOD_HASH=set_coefficients_6e86de812a
ROOST_METHOD_SIG_HASH=set_coefficients_9310de71c7

Scenario 1: The lists provided are of the correct length
Details:
  TestName: test_set_coefficients_correct_length
  Description: This test verifies if the method set_coefficients correctly sets the coefficients when given lists of a_coeffs and b_coeffs with length equal to self.order + 1.
Execution:
  Arrange: Initialise IIRFilter with order 2. Create lists a_coeffs and b_coeffs each with 3 float values.
  Act: Invoke set_coefficients on the instance of IIRFilter with a_coeffs and b_coeffs.
  Assert: Assert that the instance variables of IIRFilter for a_coeffs and b_coeffs match the ones passed to set_coefficients.
Validation:
  This test confirms that the function correctly processes valid inputs in line with the specifications.


Scenario 2: The list of coefficients a_coeffs is shorter than expected
Details:
  TestName: test_set_coefficients_short_acoeffs
  Description: This test validates the function's behavior if the given list of a_coeffs is less than self.order + 1.
Execution:
  Arrange: Initialise IIRFilter with order 2. Create a_coeffs with 2 float values, and b_coeffs with 3 float values.
  Act: Invoke set_coefficients with a_coeffs and b_coeffs.
  Assert: Confirm that ValueError is raised with a message stating that a_coeffs should have self.order + 1 elements.
Validation:
  This test checks that the method properly handles the error condition where a_coeffs is shorter than expected, as per the method's specifications.


Scenario 3: The list of coefficients a_coeffs is longer than expected
Details:
  TestName: test_set_coefficients_long_acoeffs
  Description: This test verifies if ValueError is thrown when a list a_coeffs is longer than expected.
Execution:
  Arrange: Initialise IIRFilter with order 2. Create a_coeffs with 4 float values, and b_coeffs with 3 float values.
  Act: Invoke set_coefficients with a_coeffs and b_coeffs.
  Assert: Assert that ValueError is raised with a message that a_coeffs should have self.order + 1 elements.
Validation:
  This test ensures that the method correctly handles the error condition where a_coeffs is longer than expected, adhering to the function's specifications.


Scenario 4: The list of coefficients b_coeffs is not the right length
Details:
  TestName: test_set_coefficients_incorrect_bcoeffs
  Description: This test validates the function's error handling if the provided list b_coeffs is not of length self.order + 1.
Execution:
  Arrange: Initialise IIRFilter with order 2. Create a_coeffs with 3 float values, and b_coeffs with 2 float values.
  Act: Invoke set_coefficients with a_coeffs and b_coeffs.
  Assert: Confirm that ValueError is raised with a message saying that b_coeffs should have self.order + 1 elements.
Validation:
  This test is important because it confirms that the method properly handles the error condition where b_coeffs is not of the correct length, as per the specifications of the method.
"""

# ********RoostGPT********
from __future__ import annotations
import pytest
from iir_filter import IIRFilter, set_coefficients

class Test_IirFilterSetCoefficients():

    def test_set_coefficients_correct_length(self):
        # Arrange
        filter = IIRFilter(2)
        a_coeffs = [1.0, 0.5, 2.0]
        b_coeffs = [1.3, 0.7, 2.5]

        # Act
        filter.set_coefficients(a_coeffs, b_coeffs)

        # Assert
        assert filter.a_coeffs == a_coeffs
        assert filter.b_coeffs == b_coeffs

    def test_set_coefficients_short_acoeffs(self):
        # Arrange
        filter = IIRFilter(2)
        a_coeffs = [1.0, 0.5]
        b_coeffs = [1.3, 0.7, 2.5]

        # Act & Assert
        with pytest.raises(ValueError,
                           match=r"Expected a_coeffs to have 3 elements for 2-order filter, got 2"):
            filter.set_coefficients(a_coeffs, b_coeffs)

    def test_set_coefficients_long_acoeffs(self):
        # Arrange
        filter = IIRFilter(2)
        a_coeffs = [1.0, 0.5, 2.0, 3.0]
        b_coeffs = [1.3, 0.7, 2.5]

        # Act & Assert
        with pytest.raises(ValueError,
                           match=r"Expected a_coeffs to have 3 elements for 2-order filter, got 4"):
            filter.set_coefficients(a_coeffs, b_coeffs)

    def test_set_coefficients_incorrect_bcoeffs(self):
        # Arrange
        filter = IIRFilter(2)
        a_coeffs = [1.0, 0.5, 2.0]
        b_coeffs = [1.3, 0.7]

        # Act & Assert
        with pytest.raises(ValueError,
                           match=r"Expected b_coeffs to have 3 elements for 2-order filter, got 2"):
            filter.set_coefficients(a_coeffs, b_coeffs)
