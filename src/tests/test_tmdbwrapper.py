from tmdbwrapper import TV



# testing the API call
def test_tv_info():

    tv_instance = TV(1396)
    response = tv_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == 1396, "The ID is not inside the response"
