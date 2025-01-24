from ultralytics import YOLO

model = YOLO('Models/best.pt')

results = model.predict('Input Videos/08fd33_4.mp4',save=True) # This save=True will save the video after process it(with bounding boxes and confidence levels)
print(results[0])
print("#########################################################")
for box in results[0].boxes: 
    print(box)

