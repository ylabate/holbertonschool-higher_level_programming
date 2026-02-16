#!/usr/bin/python3
import requests

if __name__ == "__main__":
    print(requests.get("https://jsonplaceholder.typicode.com/post/1"))
