import requests

def get(f) -> requests.Response:
  '''
  Function decorator for dynamic API fetching. Returns same value as `requests.Reponse`.
  
  Example definition:
  ```
  @get
  def gh_profile(username: str):
    return f'api.github.com/users/{username}'
  ```
  
  Example usage:
  ```
  print(
    "cowboycodr (id):", gh_profile("cowboycodr").json()['id']
  )
  ```
  You can now use the return object the same as `requests.Response`
  
  '''
  
  def wrapper(*args):
    return requests.get(f(*args))
    
  return wrapper