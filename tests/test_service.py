import pytest
import source.service as service
import unittest.mock as mock
import requests

@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    assert service.get_user_from_db(1) == "Mocked Alice"

@mock.patch("requests.get")
def test_get_users(mock_get):
    # mock_response is an object that mocks the requests.get() response
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'id': 1, 'name': "John Doe"}
    # use mock_response in place of the actual requests.get() response
    mock_get.return_value = mock_response
    # invoke the function being tested
    assert service.get_users() == {'id': 1, 'name': "John Doe"}

@mock.patch("requests.get")
def test_get_users_error(mock_get):
    # mock_response = mock.Mock()
    # mock_response.status_code = 400
    # rather, create the mock response object inline
    mock_get.return_value = mock.Mock(status_code=400)
    with pytest.raises(requests.HTTPError):
        service.get_users()
