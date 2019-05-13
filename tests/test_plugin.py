import mock

from pytest_circleci.plugin import pytest_collection_modifyitems


class Item:
    location = 'location'

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name



@mock.patch('pytest_circleci.plugin.hashlib')
@mock.patch('pytest_circleci.plugin.read_circleci_env_variables')
def test_first_container(read_circleci_env_variables_mock, hashlib):
    item1 = Item('item1')
    item2 = Item('item2')
    item3 = Item('item3')
    item4 = Item('item4')
    item5 = Item('item5')
    items = [item1, item2, item3, item4, item5]
    sha1 = mock.sentinel
    sha1.hexdigest = mock.Mock(side_effect=['1', '3', '2', '5', '4'])
    hashlib.sha1 = mock.Mock(return_value=sha1)
    config = mock.Mock()
    read_circleci_env_variables_mock.return_value = (2, 0)

    pytest_collection_modifyitems('session', config, items)

    config.hook.pytest_deselected.assert_called_with(items=[item3, item5])


@mock.patch('pytest_circleci.plugin.hashlib')
@mock.patch('pytest_circleci.plugin.read_circleci_env_variables')
def test_second_container(read_circleci_env_variables_mock, hashlib):
    item1 = Item('item1')
    item2 = Item('item2')
    item3 = Item('item3')
    item4 = Item('item4')
    item5 = Item('item5')
    items = [item1, item2, item3, item4, item5]
    sha1 = mock.sentinel
    sha1.hexdigest = mock.Mock(side_effect=['1', '3', '2', '5', '4'])
    hashlib.sha1 = mock.Mock(return_value=sha1)
    config = mock.Mock()
    read_circleci_env_variables_mock.return_value = (2, 1)

    pytest_collection_modifyitems('session', config, items)

    config.hook.pytest_deselected.assert_called_with(items=[item1, item2, item4])
