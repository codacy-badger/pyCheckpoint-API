import responses


@responses.activate
def test_add_tag(firewallManagement, resp_tag):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-tag",
        json=resp_tag,
        status=200,
    )

    resp = firewallManagement.network_objects.tag.add(name="My New Tag1")

    assert resp.uid == "728a4212-a521-46a2-a5a1-b6536a9aecd5"
    assert resp.name == "My New Tag1"


@responses.activate
def test_show_tag(firewallManagement, resp_tag):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-tag",
        json=resp_tag,
        status=200,
    )

    resp = firewallManagement.network_objects.tag.show(
        uid="728a4212-a521-46a2-a5a1-b6536a9aecd5"
    )

    assert resp.uid == "728a4212-a521-46a2-a5a1-b6536a9aecd5"
    assert resp.name == "My New Tag1"


@responses.activate
def test_set_tag(firewallManagement, resp_tag):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-tag",
        json=resp_tag,
        status=200,
    )

    resp = firewallManagement.network_objects.tag.set(
        uid="728a4212-a521-46a2-a5a1-b6536a9aecd5", new_name="My New Tag1"
    )

    assert resp.uid == "728a4212-a521-46a2-a5a1-b6536a9aecd5"
    assert resp.name == "My New Tag1"


@responses.activate
def test_delete_tag(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-group",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.group.delete(
        uid="728a4212-a521-46a2-a5a1-b6536a9aecd5"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_tags(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-groups",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.network_objects.group.show_groups()

    assert isinstance(resp.total, int)
