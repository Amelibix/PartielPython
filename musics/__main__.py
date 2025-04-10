"""CLI public options."""

import argparse

from . import cli
# Erreur avec float
def positive_float(value):
    f = float(value)
    if f <= 0:
        raise argparse.ArgumentTypeError(f'{value} is not a positive number')
    return f

parser = argparse.ArgumentParser(
    prog='muscis',
    description='Display various information about music',
)
parser.add_argument(
    'command',
    help='command to launch',
    choices=('artists', 'tracks', 'customers', 'search'),
)
parser.add_argument(
    '--top',
    help='number of top elements to display',
    type=positive_float,
    default=10,
)

parser.add_argument( # ajout de search pour le TDD
    '--query',
    help='text to search for (used with command "search")',
    type=str,
)

def main(argv=None):
    args = parser.parse_args(argv)
    top = args.top
    match args.command:
        case 'artists':
            cli.top_artists(top)
        case 'tracks':
            cli.top_tracks(top)
        case 'customers':
            cli.top_customers(top)
        case 'search':
            cli.search_artists(args.query)


if __name__ == '__main__':# pragma: no cover (sinon il est pris en compte dans le test )
    main()

# pour vérifier TDD :  python -m musics search --query of