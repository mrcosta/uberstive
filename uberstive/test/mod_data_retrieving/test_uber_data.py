from uberstive.mod_data_retrieving.uber_data import login, access_token, history
import vcr
import config

my_vcr = vcr.VCR(cassette_library_dir=config.TEST_DIR + '/mod_data_retrieving/fixtures/cassettes/',
                     record_mode='once',
                     filter_headers=['authorization'],
                     filter_query_parameters=['access_token'])

# TODO: make integration tests with all steps: login, code, access_token and history

@my_vcr.use_cassette()
def test_retrieve_history():
    access_token = 'n0I2cIXihQstBCDVO8h5Z8zl3FvfpA'
    request_id_history = history(access_token)

    assert len(request_id_history) == 50
    assert '941b93ea-05df-4d7d-90e0-a0f0044f5f01' and '291cd6a4-e723-4cc6-a179-cf307ecfb6b3' in request_id_history
