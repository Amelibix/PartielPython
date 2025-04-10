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
