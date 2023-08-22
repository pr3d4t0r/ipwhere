from ipwhere import die
from ipwhere import displayErrorIn
from ipwhere import displayResultsIn
from ipwhere import fetchLocationData
from ipwhere import helpUser
from ipwhere import reverseDNSOf


# +++ constants +++

TEST_IP = '1.1.1.1'
TEST_RDNS = 'one.one.one.one'


# +++ globals +++
_locationData = None


# +++ tests +++


def test_die():
    assert not die('x', 42, True)


def test_helpUser():
    assert not helpUser(unitTest = True)


def test_fetchLocationData():
    global _locationData
    status, _locationData = fetchLocationData(TEST_IP)

    assert status == 200
    assert _locationData['country_code'] == 'US'


def test_reverseDNSOf():
    assert reverseDNSOf(TEST_IP) == TEST_RDNS
    assert 'Errno 8' in reverseDNSOf(TEST_IP+'xx')


def test_displayResultsIn():
    output = displayResultsIn(_locationData, True)

    assert 'US' in output
    assert TEST_IP in output


def test_displayErrorIn():
    pass

