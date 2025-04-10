from musics import db


def test_artists():
    rows = db.get_artists()
    assert len(rows) > 270

def test_get_albums():
    rows = db.get_albums()
    assert len(rows) > 100

def test_get_tracks():
    rows = db.get_tracks()
    assert len(rows) > 1000

def test_get_playlists():
    rows = db.get_playlists()
    assert len(rows) > 10

def test_get_invoices():
    rows = db.get_invoices()
    assert len(rows) > 50

def test_get_customers():
    rows = db.get_customers()
    assert len(rows) > 50

def test_top_customers_limit():
    rows = db.get_top_customers(5)
    assert len(rows) == 5

def test_get_album_by_id():
    rows = db.get_albums(1)
    assert len(rows) == 1

def test_get_track_by_id():
    rows = db.get_tracks(1)
    assert len(rows) == 1

def test_get_playlist_by_id():
    rows = db.get_playlists(1)
    assert len(rows) == 1

def test_get_invoice_by_id():
    rows = db.get_invoices(1)
    assert len(rows) == 1

def test_get_customer_by_id():
    rows = db.get_customers(1)
    assert len(rows) == 1

def test_get_artist_by_id():
    rows = db.get_artists(1)
    assert len(rows) == 1
