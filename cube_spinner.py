import cv2
import numpy as np
import mediapipe as mp
import time
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

# importing the required pre trained models and utils from mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles



def get_hand_rotation(landmarks):

    wrist = landmarks[0]            
    middle_mcp = landmarks[9]        
    index_tip = landmarks[8]         
    pinky_mcp = landmarks[17]   
    # getting only the necessary landmarks to rotate the cube      


    # up and down motion, considering the necessary changes in landmarks when you hand moves up or down to get the pitch
    hand_pitch = (wrist.y - middle_mcp.y) * 360 # 360 here is the multipier, the greater the multipler the faster and quicker the cube moves as your hand rotates
    
    # left and right, considering the necessary changes in landmarks when you hand moves left or right to get the yaw
    hand_yaw = (index_tip.x - pinky_mcp.x) * 360
    
    # rolling motion, considering the necessary changes in landmarks when you hand rolls to get the roll
    hand_roll = (middle_mcp.x - wrist.x) * 360 


    return hand_pitch, hand_yaw, hand_roll



def draw_wireframe_cube():

    glColor3f(111/255.0, 2/255.0, 2/255.0)  # deep/cherry red color
    
    glLineWidth(2.0)
    

    vertices = [
        [-1, -1, -1],  
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, 1],     
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1]
    ]
    
  
    edges = [
        
        (0, 1), (1, 2), (2, 3), (3, 0),
    
        (4, 5), (5, 6), (6, 7), (7, 4),
    
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    
 
    glBegin(GL_LINES)
    
  
    for edge in edges:
     
        vertex1 = vertices[edge[0]]
        vertex2 = vertices[edge[1]]
        
       
        glVertex3f(vertex1[0], vertex1[1], vertex1[2])
        glVertex3f(vertex2[0], vertex2[1], vertex2[2])
    
 
    glEnd()





def draw_landmarks_on_image(image, results):

    annotated_image = image.copy()
    
    if results.multi_hand_landmarks:
        for hand_idx, hand_landmarks in enumerate(results.multi_hand_landmarks):

            mp_drawing.draw_landmarks(
                annotated_image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )
      
    
    return annotated_image


hands = mp_hands.Hands(
    static_image_mode=False,   
    max_num_hands=1,    # this makes the model only detect one hand       
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)


cap = cv2.VideoCapture(0)

# initializing all the rotations to 0 when the web cam starts
rot_x = 0  
rot_y = 0 
rot_z = 0  

print("Hand detection started. Press 'q' to quit.")


pygame.init()
display_size = (800, 600)
screen = pygame.display.set_mode(display_size, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Cube Rotation")  


gluPerspective(45, (display_size[0] / display_size[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5) 


glEnable(GL_DEPTH_TEST)
glClearColor(0.0, 0.0, 0.0, 1.0) # setting the background color as black

running = True # tracking if the program has been closed or not

while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            hands.close()
            cap.release()  
            cv2.destroyAllWindows()
            running = False    

    ret, frame = cap.read()
    if not ret:
            print("Failed to capture frame from camera")
            break
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # media pipe recognizes better in RGB mode while the default mode in open cv is BGR
    results = hands.process(rgb_frame)


    if results.multi_hand_landmarks:
      landmarks = results.multi_hand_landmarks[0].landmark
      new_rot_x, new_rot_y, new_rot_z = get_hand_rotation(landmarks)
     
    
      print(f"Rotation - X: {rot_x:6.1f}, Y: {rot_y:6.1f}, Z: {rot_z:6.1f}", end='\r') # optional print statement to see the rotations
      rot_x = new_rot_x
      rot_y = new_rot_y
      rot_z = new_rot_z

  

    annotated_frame = draw_landmarks_on_image(rgb_frame, results)
    bgr_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR)
    cv2.imshow("Hand Detection", bgr_frame) # this displays the web cam only
    
    
   
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)   
    
    glPushMatrix()

    glRotatef(rot_x, 1, 0, 0)  
    glRotatef(rot_y, 0, 1, 0)  
    glRotatef(rot_z, 0, 0, 1)  
    
    
    draw_wireframe_cube()
    
    
    glPopMatrix()
    

    pygame.display.flip() # this displays the cube on a new window

    if cv2.waitKey(1) == ord('q'):
        running = False


pygame.quit()
cap.release()
cv2.destroyAllWindows()