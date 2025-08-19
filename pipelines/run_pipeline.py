# Thin runner that calls into src/PKG_NAME/*
from PKG_NAME import hello
if __name__ == "__main__":
    print(hello())
