import cv2

# Load the image
img = cv2.imread("solar-system.jpg")

# Define the font and color for the text
font = cv2.FONT_HERSHEY_COMPLEX
color = (255, 255, 255)

# Add labels for the planets
cv2.putText(img, "Sun", (20, 300), font, 0.5, color, 1, cv2.LINE_AA)
cv2.putText(img, "Mercury", (100, 300), font, 0.5, color, 1, cv2.LINE_AA)
cv2.putText(img, "Venus", (200, 300), font, 0.5, color, 1, cv2.LINE_AA)
cv2.putText(img, "Earth", (300, 300), font, 0.5, color, 1, cv2.LINE_AA)
cv2.putText(img, "Mars", (400, 300), font, 0.5, color, 1, cv2.LINE_AA)
cv2.putText(img, "Jupiter", (600, 370), font, 0.5, color, 1, cv2.LINE_AA)
cv2.putText(img, "Saturn", (800, 320), font, 0.5, color, 1, cv2.LINE_AA)
cv2.putText(img, "Uranus", (1000, 300), font, 0.5, color, 1, cv2.LINE_AA)
cv2.putText(img, "Neptune", (1100, 300), font, 0.5, color, 1, cv2.LINE_AA)

# Display the image with the added labels
cv2.imshow("Solar System", img)

# Save the image with the added labels
cv2.imwrite("solar_system_labeled.jpg", img)

# Wait for a key press and close the window
cv2.waitKey(0)