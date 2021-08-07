"""Add this to <project-root>/mocker_over_mock.py"""

import pytest

try:
    import mock  # fails on Python 3
except ImportError:
    from unittest import mock


def first_test_fn():
    return 42


def another_test_fn():
    return 42


class TestManualMocking(object):
    """This is dangerous because we could forget to call ``stop``,
    or the test could error out; both would leak state across tests
    """

    @pytest.mark.xfail(strict=True, msg="We want this test to fail.")
    def test_manual(self):
        patcher = mock.patch("mocker_over_mock.first_test_fn", return_value=84)
        patcher.start()
        assert first_test_fn() == 42
        assert False
        patcher.stop()

    def test_manual_follow_up(self):
        assert first_test_fn() == 42, "Looks like someone leaked state!"


class TestDecoratorMocking(object):
    """This is better, but:
        1. Confusing when we start layering ``pytest`` decorators like
        ``@pytest.mark`` with ``@mock.patch``.
        2. Doesn't work when used with fixtures.
        3. Forces you to accept `mock_fn` as an argument even when the
        mock is just set up and never used in your test - more boilerplate.
    """

    @pytest.mark.xfail(strict=True, msg="We want this test to fail.")
    @mock.patch("mocker_over_mock.another_test_fn", return_value=84)
    def test_decorator(self, mock_fn):
        assert another_test_fn() == 84
        assert False

    def test_decorator_follow_up(self):
        assert another_test_fn() == 42

    @pytest.fixture
    @mock.patch("mocker_over_mock.another_test_fn", return_value=84)
    def mock_fn(self, _):
        return

    def test_decorator_with_fixture(self, mock_fn):
        assert another_test_fn() == 84, "@mock and fixtures don't mix!"


class TestMockerFixture(object):
    """This is best; the mocker fixture reduces boilerplate and
    stays out of the declarative pytest syntax.
    """

    @pytest.mark.xfail(strict=True, msg="We want this test to fail.")
    def test_mocker(self, mocker):
        mocker.patch("mocker_over_mock.another_test_fn", return_value=84)
        assert another_test_fn() == 84
        assert False

    def test_mocker_follow_up(self):
        assert another_test_fn() == 42    

    @pytest.fixture
    def mock_fn(self, mocker):
        return mocker.patch("mocker_over_mock.test_basic.another_test_fn", return_value=84)

    def test_mocker_with_fixture(self, mock_fn):
        assert another_test_fn() == 84