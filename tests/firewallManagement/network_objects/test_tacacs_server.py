import responses


@responses.activate
def test_add_tacacs_server(firewallManagement, resp_tacacs_server):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-tacacs-server",
        json=resp_tacacs_server,
        status=200,
    )

    resp = firewallManagement.network_objects.tacacs_server.add(
        name="tacacs7", server="h1"
    )

    assert resp.uid == "c9d1de16-407a-42bc-a28d-3b9d7f933766"
    assert resp.name == "tacacs7"
    assert resp.server.name == "h1"


@responses.activate
def test_show_tacacs_server(firewallManagement, resp_tacacs_server):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-tacacs-server",
        json=resp_tacacs_server,
        status=200,
    )

    resp = firewallManagement.network_objects.tacacs_server.show(
        uid="c9d1de16-407a-42bc-a28d-3b9d7f933766"
    )

    assert resp.uid == "c9d1de16-407a-42bc-a28d-3b9d7f933766"
    assert resp.name == "tacacs7"
    assert resp.server.name == "h1"


@responses.activate
def test_set_tacacs_server(firewallManagement, resp_tacacs_server):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-tacacs-server",
        json=resp_tacacs_server,
        status=200,
    )

    resp = firewallManagement.network_objects.tacacs_server.set(
        name="tacacs server",
        priority="5",
        encryption="true",
        secret_key="**secret**",
        server="d700e8d5-d010-4f37-ab14-f78f5a26426c",
        server_type="TACACS",
    )

    assert resp.uid == "c9d1de16-407a-42bc-a28d-3b9d7f933766"
    assert resp.name == "tacacs7"
    assert resp.server.name == "h1"


@responses.activate
def test_delete_tacacs_server(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-tacacs-server",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.tacacs_server.delete(
        uid="c9d1de16-407a-42bc-a28d-3b9d7f933766"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_tacacs_servers(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-tacacs-servers",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.network_objects.tacacs_server.show_tacacs_servers()

    assert isinstance(resp.total, int)
