import argparse
import string

tokenFormat = {
    ""
}

def tryReadFile(name: str):
    try:
        with open(name) as file:
            pass
    except FileNotFoundError:
        print(f"No such file: {name}")
        quit()


def __main():
    parser = argparse.ArgumentParser(description="Run a specific file.")
    parser.add_argument("file")

    args = parser.parse_args()
    print(f"file to run: {args.file}")
    tryReadFile(args.file)

if __name__ == "__main__":
    try:
        __main()
    except KeyboardInterrupt:
        quit()
    except Exception as error:
        print("An error occurred:", type(error).__name__)
    