import argparse

def parse_theme_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", help='Use dark mode.', action="store_true")
    args = parser.parse_args()
    if args.d:
        return 1
    else:
        return 0