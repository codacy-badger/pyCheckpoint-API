import responses


@responses.activate
def test_add_service_other(firewallManagement, resp_service_other):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-service-other",
        json=resp_service_other,
        status=200,
    )

    resp = firewallManagement.service_applications.service_other.add(
        name="New_Service_1",
        keep_connections_open_after_policy_installation=False,
        session_timeout=0,
        match_for_any=True,
        sync_connections_on_cluster=True,
        ip_protocol=51,
        aggressive_aging={"enable": True, "timeout": 360, "use-default-timeout": False},
    )

    assert resp.uid == "42f2b86e-09ee-415c-a6ae-75556c6c70e0"
    assert resp.name == "New_Service_1"
    assert resp.ip_protocol == 51


@responses.activate
def test_show_service_other(firewallManagement, resp_service_other):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-service-other",
        json=resp_service_other,
        status=200,
    )

    resp = firewallManagement.service_applications.service_other.show(
        uid="42f2b86e-09ee-415c-a6ae-75556c6c70e0"
    )

    assert resp.uid == "42f2b86e-09ee-415c-a6ae-75556c6c70e0"
    assert resp.name == "New_Service_1"
    assert resp.ip_protocol == 51


@responses.activate
def test_set_service_other(firewallManagement, resp_service_other):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-service-other",
        json=resp_service_other,
        status=200,
    )

    resp = firewallManagement.service_applications.service_other.set(
        uid="42f2b86e-09ee-415c-a6ae-75556c6c70e0", ip_address="192.0.2.1"
    )

    assert resp.uid == "42f2b86e-09ee-415c-a6ae-75556c6c70e0"
    assert resp.name == "New_Service_1"
    assert resp.ip_protocol == 51


@responses.activate
def test_delete_service_other(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-service-other",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.service_applications.service_other.delete(
        uid="42f2b86e-09ee-415c-a6ae-75556c6c70e0"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_services_other(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-services-other",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.service_applications.service_other.show_services_other()

    assert isinstance(resp.total, int)
