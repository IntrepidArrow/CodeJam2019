import json
import requests
import os.path
import math

def json_r(filename):
   with open(filename) as f_in:
       return(json.load(f_in))

#Check if the JSON file with datapoint resource exists
file_status = os.path.exists("D:\\CodeJam_2019\\Idea_Workspace\\CodeJam2019\\data.json")
print(file_status) 

if not file_status:
    print("In process of making a new data.json file.....")
    # Code provided in WrnchAPI Documentation
    # Wrnch Cloud API access 
    LOGIN_URL = 'https://api.wrnch.ai/v1/login'
    JOBS_URL = 'https://api.wrnch.ai/v1/jobs'
    #Save the Cloud API key for next cell to work
    API_KEY = "e0bdf9dc-50d2-4f8a-955d-e0344fb7f603"

    resp_auth = requests.post(LOGIN_URL, data={'api_key': API_KEY}) 
    print(resp_auth.text)
    # the jwt token is valid for an hour
    JWT_TOKEN = json.loads(resp_auth.text)['access_token']
    with open('D:/CodeJam_2019/' + 'thumbnail_IMG_20191116_215103.jpg', 'rb') as f:
        resp_sub_job = requests.post(JOBS_URL,
                                    headers={'Authorization': f'Bearer {JWT_TOKEN}'},
                                    files={'media': f},
                                    data={'work_type': 'json'}
                                    )

    job_id = json.loads(resp_sub_job.text)['job_id']
    print('Status code:', resp_sub_job.status_code)
    print('Response:', resp_sub_job.text)

    GET_JOB_URL = JOBS_URL + '/' + job_id
    print(GET_JOB_URL)
    
    #Request data set and store in data.json file for future use
    resp_get_job = requests.get(GET_JOB_URL, headers={'Authorization': f'Bearer {JWT_TOKEN}'})
    print('Status code:', resp_get_job.status_code)
    print('\nResponse:', resp_get_job.text)
    # Write the repsonse to a Json file to avoid repeated tokenization
    with open('D:/CodeJam_2019/Idea_Workspace/CodeJam2019/data.json', 'w', encoding="utf-8") as datafile:
        datafile.write(resp_get_job.text)


# Open data set from data.json for data processing 
with open('D:/CodeJam_2019/Idea_Workspace/CodeJam2019/data.json', mode='r', encoding='utf-8') as datafile:
    right_arm_test_estimation = json.load(datafile)

# Getting Joint datapoints - Testing
# xrightElbow = right_arm_test_estimation['frames'][0]['persons'][0]['pose2d']['joints'][22]
# yrightElbow = right_arm_test_estimation['frames'][0]['persons'][0]['pose2d']['joints'][23]
# xrightWrist = right_arm_test_estimation['frames'][0]['persons'][0]['pose2d']['joints'][20]
# yrightWrist = right_arm_test_estimation['frames'][0]['persons'][0]['pose2d']['joints'][21]
# xrightShoulder = right_arm_test_estimation['frames'][0]['persons'][0]['pose2d']['joints'][24]
# yrightShoulder = right_arm_test_estimation['frames'][0]['persons'][0]['pose2d']['joints'][25]
# xrightHip = right_arm_test_estimation['frames'][0]['persons'][0]['pose2d']['joints'][4]
# yrightHip = right_arm_test_estimation['frames'][0]['persons'][0]['pose2d']['joints'][5]

# print("Right Wrist:")
# print(xrightWrist)
# print(yrightWrist)
# print("Right Elbow: ")
# print(xrightElbow)
# print(yrightElbow)
# print("Right Shoulder:")
# print(xrightShoulder)
# print(yrightShoulder)
# print("Right Hip:")
# print(xrightHip)
# print(yrightHip)

# right_arm_test_estimation = json_r("D:/CodeJam_2019/RightArm-processed/json-RightArm.json")
# right_arm_test_estimation = json_r('D:/CodeJam_2019/thumbnail_IMG_20191116_215103-processed/json-thumbnail_IMG_20191116_215103.json')

# Data Analysis:
xRSHOULDER = right_arm_test_estimation['frames'][0]['persons'][0]['pose2d']['joints'][24]
yRSHOULDER = right_arm_test_estimation['frames'][0]['persons'][0]['pose2d']['joints'][25]

xRELBOW = right_arm_test_estimation['frames'][0]['persons'][0]['pose2d']['joints'][22]
yRELBOW = right_arm_test_estimation['frames'][0]['persons'][0]['pose2d']['joints'][23]

xRHIP = right_arm_test_estimation['frames'][0]['persons'][0]['pose2d']['joints'][4]
yRHIP = right_arm_test_estimation['frames'][0]['persons'][0]['pose2d']['joints'][5]

xRWRIST = right_arm_test_estimation['frames'][0]['persons'][0]['pose2d']['joints'][20]
yRWRIST = right_arm_test_estimation['frames'][0]['persons'][0]['pose2d']['joints'][21]

def calculate_distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

def calculate_angle(d1, d2, d3):
    angle = math.acos((d2**2 + d3**2 - d1**2)/(2*d2*d3))
    return math.degrees(angle)


distanceR_shoulder_hip = calculate_distance(xRSHOULDER, yRSHOULDER, xRHIP, yRHIP)
distanceR_shoulder_elbow = calculate_distance(xRSHOULDER, yRSHOULDER, xRELBOW, yRELBOW)
distanceR_elbow_hip = calculate_distance(xRELBOW, yRELBOW, xRHIP, yRHIP)
distanceR_elbow_wrist = calculate_distance(xRELBOW, yRELBOW, xRWRIST, yRWRIST)
distanceR_shoulder_wrist = calculate_distance(xRSHOULDER, yRSHOULDER, xRWRIST, yRWRIST)

print(distanceR_shoulder_wrist, distanceR_elbow_wrist, distanceR_shoulder_elbow)
print(distanceR_elbow_hip, distanceR_shoulder_elbow, distanceR_shoulder_hip)

# Elbow bend angle 
right_angle_1 = calculate_angle(distanceR_shoulder_wrist, distanceR_elbow_wrist, distanceR_shoulder_elbow)
print(right_angle_1)
# Arm-pit angle 
right_angle_2 = calculate_angle(distanceR_elbow_hip, distanceR_shoulder_elbow, distanceR_shoulder_hip)
print(right_angle_2)

if right_angle_1 < 80 or right_angle_2 < 80:
    print("You have a bad position.")
else:
    print("Your position is good!")
