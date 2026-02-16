#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    page = requests.get("https://jsonplaceholder.typicode.com/posts/")
    print(f"Status Code: {page.status_code}")
    print('\n'.join(post['title'] for post in page.json()))

def fetch_and_save_posts():
    res = requests.get("https://jsonplaceholder.typicode.com/posts/").json()
    data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in res]
    with open("posts.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, ['id', 'title',  'body'])
        writer.writeheader()
        writer.writerows(data)