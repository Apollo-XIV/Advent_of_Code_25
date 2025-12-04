from pathlib import Path

def get_day_input(day):
    path = Path(__file__).parent / f"../inputs/{day}.txt"
    f = open(path, 'r')
    contents = f.read()
    f.close()
    return contents
