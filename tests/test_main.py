from musics.__main__ import main


def test_artists():
    argv = ['artists']
    main(argv)

def test_tracks():
    argv = ['tracks']
    main(argv)

def test_customers():
    argv = ['customers']
    main(argv)

import pytest
from musics.__main__ import main

def test_invalid_top():
    with pytest.raises(SystemExit):
        main(['artists', '--top', '0'])
