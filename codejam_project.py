import json
from math import *

# Gets the position of each joint to be analyzed
cloud_pose_estimation = json.loads(resp_get_job.text)
cloud_xLSHOULDER = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][26]
cloud_yLSHOULDER = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][27]

cloud_xLELBOW = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][28]
cloud_yLELBOW = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][29]

cloud_xLHIP = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][6]
cloud_yLHIP = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][7]

cloud_xLWRIST = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][30]
cloud_yLWRIST = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][31]

cloud_xRSHOULDER = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][24]
cloud_yRSHOULDER = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][25]

cloud_xRELBOW = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][22]
cloud_yRELBOW = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][23]

cloud_xRHIP = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][4]
cloud_yRHIP = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][5]

cloud_xRWRIST = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][20]
cloud_yRWRIST = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][21]

def calculate_distance(x1, y1, x2, y2):
    dist = abs(sqrt((x2 - x1)**2 + (y2 - y1)**2))

    return dist

def calculate_angle(d1, d2, d3):
    angle = d1**2 = d2**2 + d3**2 - 2*a*b*cos(d1)

    return angle
    
distanceL_shoulder_hip = calculate_distance(cloud_xLSHOULDER, cloud_yLSHOULDER, cloud_xLHIP, cloud_yLHIP)
distanceL_shoulder_elbow = calculate_distance(cloud_xLSHOULDER, cloud_yLSHOULDER, cloud_xLELBOW, cloud_yLELBOW)
distanceL_elbow_hip = calculate_distance(cloud_xLELBOW, cloud_yLELBOW, cloud_xLHIP, cloud_yLHIP)
distanceL_elbow_wrist = calculate_distance(cloud_xLELBOW, cloud_yLELBOW, cloud_xLWRIST, cloud_yLWRIST)
distanceL_shoulder_wrist = calculate_distance(cloud_xLSHOULDER, cloud_yLSHOULDER, cloud_xLWRIST, cloud_yLWRIST)

distanceR_shoulder_hip = calculate_distance(cloud_xRSHOULDER, cloud_yRSHOULDER, cloud_xRHIP, cloud_yRHIP)
distanceR_shoulder_elbow = calculate_distance(cloud_xRSHOULDER, cloud_yRSHOULDER, cloud_xRELBOW, cloud_yRELBOW)
distanceR_elbow_hip = calculate_distance(cloud_xRELBOW, cloud_yRELBOW, cloud_xRHIP, cloud_yRHIP)
distanceR_elbow_wrist = calculate_distance(cloud_xRELBOW, cloud_yRELBOW, cloud_xRWRIST, cloud_yRWRIST)
distanceR_shoulder_wrist = calculate_distance(cloud_xRSHOULDER, cloud_yRSHOULDER, cloud_xRWRIST, cloud_yRWRIST)

right_angle_1 = calculate_angle(distanceR_shoulder_wrist, distanceR_elbow_wrist, distanceR_shoulder_elbow)
right_angle_2 = calculate_angle(distanceR_elbow_hip, distanceR_shoulder_elbow, distanceR_shoulder_hip)
left_angle_1 = calculate_angle(distanceL_shoulder_wrist, distanceL_elbow_wrist, distanceL_shoulder_elbow)
left_angle_2 = calculate_angle(distanceL_elbow_hip, distanceL_shoulder_elbow, distanceL_shoulder_hip)


# Analyse the 3 pictures (up, middle, down)
for i in range (3):
    
