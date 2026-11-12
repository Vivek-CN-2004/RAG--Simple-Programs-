#get Method

print("never give up")

import requests

urls = "https://jsonplaceholder.typicode.com/users/1" 

response = requests.get(url=urls)

print("response in dictionary")
print(response.json())
print("=============================================================")
print()
print(response.status_code)
print()
print(response.url)

#Post method

import requests
class Post:
    url = "https://jsonplaceholder.typicode.com/posts"
    def postData(self):
        self.headers = {
            'content-type' : 'application/json',
            'accept'       : 'application/json'
        }
        self.data = {
            'title'  : 'My first rag projrct',
            'body'   : 'Iam learning AI topics',
            'userId' :  1
        }
        self.response = requests.post(Post.url,headers=self.headers ,json = self.data)
        print(self.response.status_code)
        print("=================================")
        print(self.response.json())
p = Post()
p.postData()

