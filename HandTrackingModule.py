import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode,
                                        max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon,
                                        min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        bbox = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return lmList, bbox

    def fingersUp(self):
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[0]
            fingers = []
            # Thumb
            if myHand.landmark[4].x < myHand.landmark[3].x:
                fingers.append(1)
            else:
                fingers.append(0)
            # Fingers
            for id in range(1, 5):
                if myHand.landmark[id * 4].y < myHand.landmark[id * 4 - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)
            return fingers
        return []

    def findDistance(self, p1, p2, img, draw=True):
        if self.results.multi_hand_landmarks:
            x1, y1 = self.results.multi_hand_landmarks[0].landmark[p1].x, self.results.multi_hand_landmarks[0].landmark[p1].y
            x2, y2 = self.results.multi_hand_landmarks[0].landmark[p2].x, self.results.multi_hand_landmarks[0].landmark[p2].y
            h, w, c = img.shape
            x1, y1 = int(x1 * w), int(y1 * h)
            x2, y2 = int(x2 * w), int(y2 * h)
            length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if draw:
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                cv2.circle(img, (x1, y1), 10, (0, 255, 0), cv2.FILLED)
                cv2.circle(img, (x2, y2), 10, (0, 255, 0), cv2.FILLED)
                cv2.circle(img, ((x1 + x2) // 2, (y1 + y2) // 2), 10, (0, 255, 0), cv2.FILLED)
            return length, img, [x1, y1, x2, y2, (x1 + x2) // 2, (y1 + y2) // 2]
        return 0, img, [0, 0, 0, 0, 0, 0]
