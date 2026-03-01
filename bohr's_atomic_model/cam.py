import time

import cv2
import mediapipe as mp
import numpy as np

import state

cap = cv2.VideoCapture(0)


def draw_hud(frame):
    PINK = (180, 20, 255)
    PURPLE = (220, 50, 180)
    BLUE = (255, 140, 30)
    LAVENDER = (255, 180, 200)
    DARK = (20, 10, 30)

    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    font_bold = cv2.FONT_HERSHEY_COMPLEX

    h, w = frame.shape[:2]
    cx = w // 2  # center x

    box_w = 325
    box_h = 180
    x1 = cx - box_w // 2
    x2 = cx + box_w // 2
    y1 = h // 2 - box_h // 2
    y2 = h // 2 + box_h // 2

    overlay = frame.copy()
    cv2.rectangle(overlay, (x1, y1), (x2, y2), DARK, -1)
    cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)

    cv2.rectangle(frame, (x1, y1), (x2, y2), PINK, 1)
    cv2.rectangle(frame, (x1 + 3, y1 + 3), (x2 - 3, y2 - 3), PURPLE, 1)

    cv2.putText(
        frame, "Bohr's Atom Model Sim", (x1 + 13, y1 + 32), font_bold, 0.65, PINK, 2
    )
    cv2.line(frame, (x1 + 10, y1 + 42), (x2 - 10, y1 + 42), PURPLE, 1)

    cv2.putText(frame, "++++ Electrons ----", (x1 + 15, y1 + 80), font, 0.85, PURPLE, 1)
    cv2.putText(frame, "++++ Neutrons  ----", (x1 + 15, y1 + 115), font, 0.85, BLUE, 1)
    cv2.putText(
        frame, "++++ Protons   ----", (x1 + 15, y1 + 150), font, 0.85, LAVENDER, 1
    )

    return frame, x1, y1


mp_hands = mp.tasks.vision.HandLandmarksConnections
mp_drawing = mp.tasks.vision.drawing_utils
mp_drawing_styles = mp.tasks.vision.drawing_styles


def draw_landmarks_on_image(rgb_image, detection_result):
    hand_landmarks_list = detection_result.hand_landmarks
    annotated_image = np.copy(rgb_image)

    for idx in range(len(hand_landmarks_list)):
        hand_landmarks = hand_landmarks_list[idx]

        mp_drawing.draw_landmarks(
            annotated_image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style(),
        )

    return annotated_image


model_path = "/foo/bar/hand_landmarker.task"


BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.IMAGE,
    num_hands=1,
    min_hand_detection_confidence=0.1,
)


def main():
    with HandLandmarker.create_from_options(options) as landmarker:
        while True:
            ret, frame = cap.read()

            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
            results = landmarker.detect(mp_image)

            if results.hand_landmarks:
                landmark = results.hand_landmarks[0][8]
                x = landmark.x
                y = landmark.y

                h, w = frame.shape[:2]
                pixel_x = int(x * w)
                pixel_y = int(y * h)

                cx = w // 2
                box_w = 325
                box_h = 180
                x1 = cx - box_w // 2
                y1 = h // 2 - box_h // 2

                rows = {
                    "Electrons": y1 + 80,
                    "Neutrons": y1 + 115,
                    "Protons": y1 + 150,
                }
                tolerance = 18
                plus_x_range = (x1 + 15, x1 + 85)
                minus_x_range = (x1 + 205, x1 + 275)

                if time.time() - state.last_action > state.cooldown:
                    for var, text_y in rows.items():
                        if abs(pixel_y - text_y) < tolerance:
                            if plus_x_range[0] <= pixel_x <= plus_x_range[1]:
                                if var == "Electrons":
                                    state.ELECTRONS = max(0, state.ELECTRONS + 1)
                                elif var == "Neutrons":
                                    state.NEUTRONS = max(0, state.NEUTRONS + 1)
                                elif var == "Protons":
                                    state.PROTONS = max(0, state.PROTONS + 1)
                            elif minus_x_range[0] <= pixel_x <= minus_x_range[1]:
                                if var == "Electrons":
                                    state.ELECTRONS = max(0, state.ELECTRONS - 1)
                                elif var == "Neutrons":
                                    state.NEUTRONS = max(0, state.NEUTRONS - 1)
                                elif var == "Protons":
                                    state.PROTONS = max(0, state.PROTONS - 1)
                            state.last_action = time.time()
                            break

            frame = draw_landmarks_on_image(frame, results)
            frame, _, _ = draw_hud(frame)
            cv2.imshow("Frame", frame)

            if cv2.waitKey(1) == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
