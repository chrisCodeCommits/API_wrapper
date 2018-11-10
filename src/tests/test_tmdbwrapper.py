
from pytest import fixture
from tmdbwrapper import TV




@fixture
# to return test data / see line 34
def tv_keys():

    return [

    'id',
    'origin_country',
    'poster_path',
    'name',
    'overview',
    'popularity',
    'backdrop_path',
    'first_air_date',
    'vote_count',
    'vote_average'

    ]



# testing the API call
def test_tv_info(tv_keys):

    tv_instance = TV(1396)
    response = tv_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == 1396, "The ID is not inside the response"
    assert set(tv_keys).issubset(response.keys()), "some keys are missing in this response"
