from uberstive.mod_data_retrieving.uber_data import user_history

def test_retrieve_user_history():
    history = user_history()
    assert history.history.size() == 224
