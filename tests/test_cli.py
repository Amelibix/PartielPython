from io import StringIO

from musics import cli


def test_top_artists():
    string = StringIO()
    cli.top_artists(file=string)
    text = string.getvalue()
    assert 'Top' in text


def test_top_tracks():
    string = StringIO()
    cli.top_tracks(file=string)
    text = string.getvalue()
    assert 'Top' in text
    assert 'tracks' in text.lower()

def test_top_customers():
    string = StringIO()
    cli.top_customers(file=string)
    text = string.getvalue()
    assert 'Top' in text
    assert 'customers' in text.lower()
