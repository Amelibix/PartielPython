from fastapi.testclient import TestClient

from musics import api


client = TestClient(api.app)


def test_artists():
    response = client.get('/artists/')
    assert response.status_code == 200
    assert len(response.json()) > 100

def test_albums():
    response = client.get('/albums/')
    assert response.status_code == 200

def test_tracks():
    response = client.get('/tracks/')
    assert response.status_code == 200

def test_playlists():
    response = client.get('/playlists/')
    assert response.status_code == 200

def test_invoices():
    response = client.get('/invoices/')
    assert response.status_code == 200

def test_customers():
    response = client.get('/customers/')
    assert response.status_code == 200

def test_album_tracks():
    response = client.get('/album_tracks/1')
    assert response.status_code == 200

def test_playlist_tracks():
    response = client.get('/playlist_tracks/1')
    assert response.status_code == 200

def test_top_artists():
    response = client.get('/top_artists/')
    assert response.status_code == 200

def test_top_tracks():
    response = client.get('/top_tracks/')
    assert response.status_code == 200

def test_top_customers():
    response = client.get('/top_customers/')
    assert response.status_code == 200


# test de correction de bug

def test_top_customers_limit():
    response = client.get("/top_customers/?top=3")
    assert response.status_code == 200
    assert len(response.json()) == 3
