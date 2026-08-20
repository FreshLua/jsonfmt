import argparse
from formatter import pretty_format, minify
from validator import validate

def main():
    parser = argparse.ArgumentParser(
        description="Instant JSON Formatter CLI"
    )

    parser.add_argument("file", help="Path to JSON file")
    parser.add_argument("--minify", action="store_true", help="Minify JSON")
    parser.add_argument("--validate", action="store_true", help="Validate JSON")
    parser.add_argument("--color", action="store_true", help="Colorize output")

    args = parser.parse_args()

    try:
        with open(args.file, "r") as f:
            data = f.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return

    if args.validate:
        print("Valid JSON" if validate(data) else "Invalid JSON")
        return

    try:
        output = minify(data) if args.minify else pretty_format(data)
    except ValueError as e:
        print(e)
        return

    if args.color:
        try:
            from pygments import highlight
            from pygments.lexers import JsonLexer
            from pygments.formatters import TerminalFormatter
            output = highlight(output, JsonLexer(), TerminalFormatter())
        except ImportError:
            print("Install pygments for color output: pip install pygments")

    print(output)

if __name__ == "__main__":
    main()
