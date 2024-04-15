from project import zip_to_location
from project import zip_to_time
from project import call_weather
import pytest
import requests
import sys



def test_zip_to_location():
    assert type(zip_to_location({"zip":"44133"})) is dict
    with pytest.raises(SystemExit):
        zip_to_location({"zip":"00000"})
    with pytest.raises(SystemExit):
        zip_to_location({"zip":"111111"})

def test_zip_to_time():
    assert type(zip_to_time({"longitude":"-81.7457","city":"North Royalton","latitude":"41.3232",})) is dict
    with pytest.raises(TypeError):
        zip_to_time({"longitude":None,"city":None,"latitude":None})



def test_call_weather():
    assert type(zip_to_time({"longitude":"-81.74","city":"North Royalton","latitude":"41.32",})) is dict
    with pytest.raises(TypeError):
        zip_to_time({"longitude":None,"city":"North Royalton","latitude":"41.3232",})


