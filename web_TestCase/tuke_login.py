import requests

# data = {
#     'access_token':'eyJhbGciOiJITUFDU0hBMjU2IiwiaXNzIjoiRWFzeVN3b29sZSIsImV4cCI6MTYwODk2OTg0Nywic3ViIjpudWxsLCJuYmYiOjE1Nzc0MzM4NDcsImF1ZCI6bnVsbCwiaWF0IjoxNTc3NDMzODQ3LCJqdGkiOiJCSDNoakxtdEE5Iiwic2lnbmF0dXJlIjoiNDI1NDlhMWZhMTljYjI0ZjljYTJiZGNkMjBiYzBiMjk3YTQ5M2QxNmQwY2MxNjVhYWFlNmE4MGUwOWU0MDlkYSIsInN0YXR1cyI6MSwiZGF0YSI6IjJpanU0cnhqYXQifQ%3D%3D'
# }
# r = requests.post('http://api.tuke.huakmall.com/group/group/list',data=data)
# print(r.json())

# rs = requests.post('http://api.tuke.huakmall.com/group/group/push',data={
#     'access_token':'eyJhbGciOiJITUFDU0hBMjU2IiwiaXNzIjoiRWFzeVN3b29sZSIsImV4cCI6MTYwODk2OTg0Nywic3ViIjpudWxsLCJuYmYiOjE1Nzc0MzM4NDcsImF1ZCI6bnVsbCwiaWF0IjoxNTc3NDMzODQ3LCJqdGkiOiJCSDNoakxtdEE5Iiwic2lnbmF0dXJlIjoiNDI1NDlhMWZhMTljYjI0ZjljYTJiZGNkMjBiYzBiMjk3YTQ5M2QxNmQwY2MxNjVhYWFlNmE4MGUwOWU0MDlkYSIsInN0YXR1cyI6MSwiZGF0YSI6IjJpanU0cnhqYXQifQ%3D%3D',
#     'tid':'2736487157',
#     'members':'infoh1m5h'
#
# })
# print(rs.json())
# r = requests.post('http://api.tuke.huakmall.com/user/appAuth/preAuthCode',data={
#     'sign':'MjJGGtHj%2B%2B4MrVSP466CfJu%2BiBCU2GYk6z0kwUyiYFQ%3D',
#     'access_token':'eyJhbGciOiJITUFDU0hBMjU2IiwiaXNzIjoiRWFzeVN3b29sZSIsImV4cCI6MTYwODk4MDA1NCwic3ViIjpudWxsLCJuYmYiOjE1Nzc0NDQwNTQsImF1ZCI6bnVsbCwiaWF0IjoxNTc3NDQ0MDU0LCJqdGkiOiJDN1BqQndnb3BWIiwic2lnbmF0dXJlIjoiZWEyNWMwYjYwMjc4YzNjODA5YzFkNTQzYWVjNjQ2NTMxYjhhMDkyNjQwZTZhMmYyMjJmOTU4ZTA2ZmViNWVmZSIsInN0YXR1cyI6MSwiZGF0YSI6IjJpanU0cnhqYXQifQ%3D%3D'
# })
# print(r.json())
r = requests.post('http://api.tuke.huakmall.com/user/appAuth/authCode',data={
    'code':'nf4CxJDTs3tP6bye',
    'access_token': 'eyJhbGciOiJITUFDU0hBMjU2IiwiaXNzIjoiRWFzeVN3b29sZSIsImV4cCI6MTYwODk4MDA1NCwic3ViIjpudWxsLCJuYmYiOjE1Nzc0NDQwNTQsImF1ZCI6bnVsbCwiaWF0IjoxNTc3NDQ0MDU0LCJqdGkiOiJDN1BqQndnb3BWIiwic2lnbmF0dXJlIjoiZWEyNWMwYjYwMjc4YzNjODA5YzFkNTQzYWVjNjQ2NTMxYjhhMDkyNjQwZTZhMmYyMjJmOTU4ZTA2ZmViNWVmZSIsInN0YXR1cyI6MSwiZGF0YSI6IjJpanU0cnhqYXQifQ%3D%3D'
})
print(r.json())
