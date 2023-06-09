#!/usr/bin/python3
if __name__ == "__main__":

    import hidden_4

    def print_names():
        name = dir(hidden_4)

        for i in name:
            if not i.startswith('__'):
                print(i)


print_names()
