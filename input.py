import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input',type=argparse.FileType('r'),required=True)
args = parser.parse_args()
print(args.input.readlines())