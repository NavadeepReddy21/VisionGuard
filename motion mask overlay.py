import cv2
import numpy as np
import time

# ==========================
# Video Input
# ==========================
video_path = r"sample.webm"  # Replace with your video file

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# ==========================
# Video Properties
# ==========================
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# ==========================
# Save Output Video
# ==========================
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(
    "motion_output.mp4",
    fourcc,
    fps,
    (width, height)
)

# ==========================
# Background Subtractor
# ==========================
fgbg = cv2.createBackgroundSubtractorMOG2(
    history=500,
    varThreshold=50,
    detectShadows=False
)

# ==========================
# FPS Calculation
# ==========================
prev_time = time.time()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # ==========================
    # Foreground Mask
    # ==========================
    mask = fgbg.apply(frame)

    # Remove Noise
    mask = cv2.medianBlur(mask, 5)

    kernel = np.ones((5, 5), np.uint8)

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        kernel
    )

    # ==========================
    # Find Contours
    # ==========================
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    overlay = np.zeros_like(frame)

    motion_count = 0

    for contour in contours:

        area = cv2.contourArea(contour)

        if area < 1000:
            continue

        motion_count += 1

        # Red motion mask
        cv2.drawContours(
            overlay,
            [contour],
            -1,
            (0, 0, 255),
            thickness=-1
        )

        # Bounding Box
        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Area: {int(area)}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2
        )

    # ==========================
    # Overlay Motion Mask
    # ==========================
    alpha = 0.5

    output = cv2.addWeighted(
        frame,
        1,
        overlay,
        alpha,
        0
    )

    # ==========================
    # FPS Counter
    # ==========================
    current_time = time.time()

    fps_display = 1 / (current_time - prev_time)

    prev_time = current_time

    cv2.putText(
        output,
        f"FPS: {int(fps_display)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.putText(
        output,
        f"Moving Objects: {motion_count}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    # ==========================
    # Save Video
    # ==========================
    out.write(output)

    # ==========================
    # Display
    # ==========================
    cv2.imshow("Motion Detection System", output)
    cv2.imshow("Foreground Mask", mask)

    key = cv2.waitKey(30)

    if key == 27:  # ESC key
        break

# ==========================
# Cleanup
# ==========================
cap.release()
out.release()

cv2.destroyAllWindows()

print("Processing completed.")
print("Output saved as motion_output.mp4")