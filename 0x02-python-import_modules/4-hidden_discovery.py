#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for attr in dir(hidden_4):
        if not attr.startswith("__"):
            print(attr)
