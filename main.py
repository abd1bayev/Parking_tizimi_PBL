from cli import run


if __name__ == "__main__":
    # Only run interactive CLI when stdin is a TTY (prevents running during automated tests)
    import sys

    if sys.stdin.isatty():
        run()
