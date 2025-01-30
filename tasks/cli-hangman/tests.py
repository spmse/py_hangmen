from hangman import display_word

def test_display_banana():
    # Arrange -> prepare the scenario: create vars, etc.
    banana_test = ("banana", "a", "_a_a_a")
    # Act -> the actual test happens with prepared info from 'arrange'
    banana_test_result_init = display_word(banana_test[0], banana_test[1])
    # Assert -> matching the actual with the expected results for the testcase
    assert banana_test[2] == banana_test_result_init, "The actual result did not match the expected result"

def test_display_apple():
    # Arrange -> prepare the scenario: create vars, etc.
    banana_test = ("apple", "a", "a____")
    # Act -> the actual test happens with prepared info from 'arrange'
    banana_test_result_init = display_word(banana_test[0], banana_test[1])
    # Assert -> matching the actual with the expected results for the testcase
    assert banana_test[2] == banana_test_result_init, "The actual result did not match the expected result"

def test_display_car():
    # Arrange -> prepare the scenario: create vars, etc.
    banana_test = ("car", "a", "_a_")
    # Act -> the actual test happens with prepared info from 'arrange'
    banana_test_result_init = display_word(banana_test[0], banana_test[1])
    # Assert -> matching the actual with the expected results for the testcase
    assert banana_test[2] == banana_test_result_init, "The actual result did not match the expected result"
    
def test_display_house():
    # Arrange -> prepare the scenario: create vars, etc.
    banana_test = ("house", "x", "_____")
    # Act -> the actual test happens with prepared info from 'arrange'
    banana_test_result_init = display_word(banana_test[0], banana_test[1])
    # Assert -> matching the actual with the expected results for the testcase
    assert banana_test[2] == banana_test_result_init, "The actual result did not match the expected result"




if __name__ == "__main__":
    test_display_banana()
    test_display_apple()
    test_display_car()
    test_display_house()
    print("tests successful")