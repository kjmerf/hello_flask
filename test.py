from unittest.mock import Mock, patch

from nose.tools import assert_is_none, assert_dict_equal

from app.app import get_data


valid_response = {'q': 'chicken',
                  'hits': [
                      {'recipe':
                          {'label': 'http://www.edamam.com/recipe_123',
                           'source': 'Blog',
                           'url': 'http://www.blog.com/recipes/chicken.html',
                           'image': 'https://www.edamam.com/web-img/123.jpg'}}
                      ]
                  }


@patch('app.app.requests.get')
def test_get_data_with_valid_key(mock_get):

    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = valid_response

    response = get_data('test_query', 'test_app_id', 'test_app_key')

    assert_dict_equal(response, valid_response)


@patch('app.app.requests.get')
def test_get_data_with_invalid_key(mock_get):

    mock_get.return_value = Mock(status_code=401)

    response = get_data('test_query', 'test_app_id', 'test_app_key')

    assert_is_none(response)
