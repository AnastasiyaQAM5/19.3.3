import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

base_url = f"https://petstore.swagger.io/v2/"
headers = {'Content-Type': 'application/json'}

#GET-запросы:

print('Start request pets')

data = MultipartEncoder(
  fields={
    'additionalMetadata': 'test',
    'file': ("1200px-Stray_kitten_Rambo002.jpg", open('tests/images/1200px-Stray_kitten_Rambo002.jpg', 'rb'), 'image/jpeg')
  })
headers_for_upload = {'Content-Type': data.content_type}

res = requests.post(base_url+'pet/9223372036854252578/uploadImage', headers=headers_for_upload, data=data)
print('Request POST: ' + res.url + '\n' + "Resnpose: " + res.text + '\n')

####################

res = requests.post(base_url+'pet', json={'name': 'name', 'status': 'available'})
print('Request POST: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

res = requests.put(base_url+'pet', json={'name': 'name', 'status': 'available'})
print('Request PUT: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

res = requests.get(base_url+'pet/findByStatus', headers=headers, params={'status': 'available'})
print('Request GET: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

res = requests.get(base_url+'pet/9223372036854306048', headers=headers)
print('Request GET: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

res = requests.post(base_url+'pet/9223372036854306048', data={'name': 'name', 'status': 'status'})
print('Request POST: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

res = requests.delete(base_url+'pet/9223372036854306048')
print('Request DELETE: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

print('Finish request pets\n')
print('Start request store\n')

res = requests.post(base_url+'store/order', json={'status': 'status', 'complete': 'true'})
print('Request POST: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

res = requests.get(base_url+'store/order/1', headers=headers)
print('Request GET: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

res = requests.delete(base_url+'store/order/1')
print('Request DELETE: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

res = requests.get(base_url+'store/inventory', headers=headers)
print('Request GET: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

print('Finish request store\n')
print('Start request users\n')

res = requests.post(base_url+'user/createWithArray', json=[{
  "id": 0,
  "username": "username2",
  "firstName": "name",
  "lastName": "name",
  "email": "test2@test.com",
  "password": "password2",
  "phone": "none",
  "userStatus": 0
}])
print('Request POST: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

res = requests.post(base_url+'user/createWithList', json=[{
  "id": 0,
  "username": "username2",
  "firstName": "name",
  "lastName": "name",
  "email": "test2@test.com",
  "password": "password2",
  "phone": "none",
  "userStatus": 0
}])
print('Request POST: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

res = requests.get(base_url+'user/username2', headers=headers)
print('Request GET: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

res = requests.put(base_url+'user/username2', json={"email": "test2@test.com"})
print('Request PUT: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

res = requests.delete(base_url+'user/username2')
print('Request DELETE: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

res = requests.get(base_url+'user/login', headers=headers, params={'username': 'username1', 'password' : 'password1'})
print('Request GET: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

res = requests.get(base_url+'user/logout', headers=headers)
print('Request GET: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

res = requests.post(base_url+'user', json={
  "id": 0,
  "username": "username1",
  "firstName": "name",
  "lastName": "name",
  "email": "test1@test.com",
  "password": "password1",
  "phone": "none",
  "userStatus": 0
})
print('Request POST: ' + res.url + '\n' + "Response: " + res.text + '\n')

####################

print('Finish request user\n')
