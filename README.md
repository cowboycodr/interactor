# Interactor
Interacting with APIs is hard. That's why Interactor. Extremely simple utilities for developer API interactions.

## Examples
```python
from interactor import Interator

class GitHub(Interactor):
  def __init__(self):
    super().__init__("https://api.github.com/")
    
  def user(self, name: str):
    return self.get(["users", name])
    
if __name__ == '__main__':
  gh = GitHub()
  
  gh.user("cowboycodr")
```
