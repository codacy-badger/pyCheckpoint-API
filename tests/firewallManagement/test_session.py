from box import Box
import responses
import pytest

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_login_username_password(firewallManagement, session):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/login",
        json=session,
        status=200,
    )

    resp = firewallManagement.session.login(
        user="test@example.com",
        password="hunter2",
        domain="MyDomain",
    )

    assert isinstance(resp, Box)
    assert resp.sid == "97BVpRfN4j81ogN-V2XqGYmw3DDwIhoSn0og8PiKDiM"


@responses.activate
def test_login_api_key(firewallManagement, session):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/login",
        json=session,
        status=200,
    )

    resp = firewallManagement.session.login(api_key="FFl8+KF1AJ2Tisac6d0K+w==")

    assert isinstance(resp, dict)
    assert resp.sid == "97BVpRfN4j81ogN-V2XqGYmw3DDwIhoSn0og8PiKDiM"


@responses.activate
def test_login_missing_mandatory_parameters(firewallManagement, session):

    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.session.login(username="User1")
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.session.login(password="Password1")


@responses.activate
def test_logout(firewallManagement, resp_message_ok):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/logout",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.session.logout()

    assert resp.message == "OK"


@responses.activate
def test_publish(firewallManagement, resp_task):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/publish",
        json=resp_task,
        status=200,
    )

    resp = firewallManagement.session.publish()

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"


@responses.activate
def test_discard(firewallManagement, resp_message_ok_with_number_of_discarded_changes):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/discard",
        json=resp_message_ok_with_number_of_discarded_changes,
        status=200,
    )

    resp = firewallManagement.session.discard()

    assert resp.message == "OK"


@responses.activate
def test_disconnect(firewallManagement, resp_message_ok):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/disconnect",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.session.disconnect(
        uid="7a13a360-9b24-40d7-acd3-5b50247be33e"
    )

    assert resp.message == "OK"


@responses.activate
def test_keepalive(firewallManagement, resp_message_ok):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/keepalive",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.session.keepalive()

    assert resp.message == "OK"


@responses.activate
def test_revert_to_revision(firewallManagement, resp_task):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/revert-to-revision",
        json=resp_task,
        status=200,
    )

    resp = firewallManagement.session.revert_to_revision()

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"


@responses.activate
def test_verify_revert(firewallManagement, resp_task):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/verify-revert",
        json=resp_task,
        status=200,
    )

    resp = firewallManagement.session.verify_revert(
        to_session="d49ed10c-649a-476a-8e80-8282eda00e15"
    )

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"


@responses.activate
def test_login_to_domain(firewallManagement, session):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/login-to-domain",
        json=session,
        status=200,
    )

    resp = firewallManagement.session.login_to_domain(domain="AnotherDomain")

    assert isinstance(resp, Box)
    assert resp.sid == "97BVpRfN4j81ogN-V2XqGYmw3DDwIhoSn0og8PiKDiM"


@responses.activate
def test_show_session(firewallManagement, resp_session):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-session",
        json=resp_session,
        status=200,
    )

    resp = firewallManagement.session.show_session()

    assert resp.uid == "7a13a360-9b24-40d7-acd3-5b50247be33e"


@responses.activate
def test_set_session(firewallManagement, resp_session):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-session",
        json=resp_session,
        status=200,
    )

    resp = firewallManagement.session.set_session(
        description="This is my new description"
    )

    assert resp.uid == "7a13a360-9b24-40d7-acd3-5b50247be33e"


@responses.activate
def test_purge_published_sessions(firewallManagement, resp_task):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/purge-published-sessions",
        json=resp_task,
        status=200,
    )

    resp = firewallManagement.session.purge_published_sessions(
        number_of_sessions_to_preserve=5
    )

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"

    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.session.purge_published_sessions()


@responses.activate
def test_switch_session(firewallManagement, resp_session):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/switch-session",
        json=resp_session,
        status=200,
    )

    resp = firewallManagement.session.switch_session(
        uid="7a13a360-9b24-40d7-acd3-5b50247be33e"
    )

    assert resp.uid == "7a13a360-9b24-40d7-acd3-5b50247be33e"


@responses.activate
def test_take_over_session(firewallManagement, resp_session):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/take-over-session",
        json=resp_session,
        status=200,
    )

    resp = firewallManagement.session.take_over_session(
        uid="7a13a360-9b24-40d7-acd3-5b50247be33e"
    )

    assert resp.uid == "7a13a360-9b24-40d7-acd3-5b50247be33e"


@responses.activate
def test_show_sessions(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-sessions",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.session.show_sessions()

    assert isinstance(resp.total, int)


@responses.activate
def test_continue_session_in_smartconsole(firewallManagement, resp_message_ok):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/continue-session-in-smartconsole",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.session.continue_session_in_smartconsole()

    assert resp.message == "OK"


@responses.activate
def test_show_last_published_session(firewallManagement, resp_session):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-last-published-session",
        json=resp_session,
        status=200,
    )

    resp = firewallManagement.session.show_last_published_session()

    assert resp.uid == "7a13a360-9b24-40d7-acd3-5b50247be33e"


@responses.activate
def test_show_login_message(firewallManagement, resp_login_message):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-login-message",
        json=resp_login_message,
        status=200,
    )

    resp = firewallManagement.session.show_login_message()

    assert resp.message == "C"


@responses.activate
def test_set_login_message(firewallManagement, resp_login_message):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-login-message",
        json=resp_login_message,
        status=200,
    )

    resp = firewallManagement.session.set_login_message(header="D")

    assert resp.header == "D"


@responses.activate
def test_set_automatic_purge(firewallManagement, resp_automatic_purge):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-automatic-purge",
        json=resp_automatic_purge,
        status=200,
    )

    resp = firewallManagement.session.set_automatic_purge(
        enabled=True, number_of_sessions_to_keep=10
    )

    assert resp.enabled is True
    assert resp.number_of_sessions_to_keep == "10"


@responses.activate
def test_show_automatic_purge(firewallManagement, resp_automatic_purge):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-automatic-purge",
        json=resp_automatic_purge,
        status=200,
    )

    resp = firewallManagement.session.show_automatic_purge()

    assert resp.enabled is True
    assert resp.number_of_sessions_to_keep == "10"
