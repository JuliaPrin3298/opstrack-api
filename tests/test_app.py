import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client


def test_home_returns_active_status(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.get_json() == {'status': 'active'}


def test_status_returns_active_status(client):
    response = client.get('/status')

    assert response.status_code == 200
    assert response.get_json() == {'status': 'active'}


def test_tickets_returns_expected_list(client):
    response = client.get('/tickets')

    assert response.status_code == 200
    tickets = response.get_json()
    assert len(tickets) == 3
    assert tickets[0] == {
        'id': 1,
        'titulo': 'Erro no login',
        'status': 'aberto',
    }
    assert tickets[1]['status'] == 'em andamento'
    assert tickets[2]['status'] == 'fechado'


def test_about_returns_api_information(client):
    response = client.get('/sobre')

    assert response.status_code == 200
    assert response.get_json() == {'nome': 'Minha API', 'versao': '1.0.0'}
