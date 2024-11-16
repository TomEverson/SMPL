import sys
from smpl import SmplProcessor


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <file.smpl> --<mode>")
        return

    file_path = sys.argv[1]
    options = sys.argv[2]



    compiler = SmplProcessor(mode=options)

    compiler.run_file(file_path)


if __name__ == "__main__":
    main()
