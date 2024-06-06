import argparse
from . import __version__

def main():
    parser = argparse.ArgumentParser(description='My Package Command Line Interface')
    parser.add_argument('--version', action='store_true', help='Print the version of the package')
    
    args = parser.parse_args()
    
    if args.version:
        print(f'my_package version {__version__}')

if __name__ == '__main__':
    main()
