from ultralytics import YOLO

# class Vid_Infer:
#     def __int__(self):
#         # Model (pretrained YOLO26n model)
#         model = YOLO("yolo26n.pt")
#         train_results = model.train(
#             data="coco8.yaml",  # Path to dataset configuration file
#             epochs=100,  # Number of training epochs
#             imgsz=640,  # Image size for training
#             device="cpu",  # Device to run on (e.g., 'cpu', 0, [0,1,2,3])
#         )
#         # Evaluate the model's performance on the validation set
#         metrics = train_results.val()

#         # Export the model to ONNX format for deployment
#         path = train_results.export(format="onnx")  # Returns the path to the exported model

#         # Perform object detection on an image
#         results = model("./1.jpg")  # Predict on an image
#         results[0].show()  # Display results