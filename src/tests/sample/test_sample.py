import pytest
import allure
@allure.step("Step 1")
@allure.title("Verify 🛑 Failed !that the Framework is working")
def test_sample_pass():
    assert True == False

@allure.title("Verify ✅ Passed that the Framework is working")
@allure.step("Step 2")
def test_sample_fail():
    assert True == True