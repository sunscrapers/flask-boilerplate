from tests import factories


def test_get_should_return_documents(client, session):
    documents_count = 3
    factories.DocumentFactory.create_batch(documents_count)

    response = client.get('/documents')

    assert response.status_code == 200
    assert len(response.json) == documents_count


def test_get_should_return_paginated_documents(client, session):
    documents_count = 3
    factories.DocumentFactory.create_batch(documents_count)
    length = 2
    start = 0

    response = client.get('/documents?start={0}&length={1}'.format(start, length))

    assert response.status_code == 200
    assert len(response.json) == length


def test_get_documents_should_return_404_when_missing_page(client, session):
    documents_count = 3
    factories.DocumentFactory.create_batch(documents_count)

    response = client.get('/documents?start=3')

    assert response.status_code == 404
    assert response.json == {}


def test_get_should_return_one_document(client, session):
    name = 'John'
    document = factories.DocumentFactory.create(data={'name': name})

    response = client.get('/documents/{id}'.format(id=document.id))

    assert response.status_code == 200
    assert response.json['name'] == name
