import requests
ENDPOINT = "https://todo.pixegami.io"

def test_verify_endpoint():
  response = requests.get(ENDPOINT verify=False)
  assert response.status_code == 200
  pass
  
 def test_create_task():
  payload = {"content": "test_content","user_id": "user001", "task_id": "task001", "is_done": False,}
  response = requests.put(ENDPOINT+"/create-task", json=payload)
  assert response.status_code == 200
  data = response.json()
  print(data)
  pass
