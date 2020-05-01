import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("hoge", help="hogehogehoge")
    args = parser.parse_args()
    print(args.hoge)

if __name__ ==  "__main__":
    main()
