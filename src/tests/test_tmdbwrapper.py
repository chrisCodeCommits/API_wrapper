
from pytest import fixture
from tmdbwrapper import TV

import vcr



'''
@vcr.use_cassette('tests/vcr_cassettes/tv-info.yml')


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



# testing the API call to get info
def test_tv_info(tv_keys):

    tv_instance = TV(1396)
    response = tv_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == 1396, "The ID is not inside the response"
    assert set(tv_keys).issubset(response.keys()), "some keys are missing in this response"

'''



@vcr.use_cassette(
    'tests/vcr_cassettes/tv-popular.yml',
    filter_query_parameters=['api_key']
    )

# testing the API call to get most popular show
def test_tv_popular():


    response = TV.popular()

    assert isinstance(response, dict)
    assert isinstance(response['results'], list)
    assert isinstance(response['results'][0], dict)
    assert set(tv_keys).issubset(response['results'][0].keys())
