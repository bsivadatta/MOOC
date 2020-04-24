# MOOC
Codes towards trying to make MOOCs a better place.

Data 
	For CNN 
    	Train      : https://drive.google.com/open?id=1fMh_ZDuN7rPmh8wZlLOFk2Zb0clGmshB
    	Validation : https://drive.google.com/open?id=1rVs-5NZYGJ0n7dPOmJ1gyVfvQ2N6TehC
  	For Custom YOLO
		https://drive.google.com/open?id=1U-3AgSJ7H_CvMonSews_wN5nwS98nOgY
Video Source :
	Power system Analysis videos used for text processing : https://nptel.ac.in/courses/117/105/117105140/
	C-Programming videos : https://nptel.ac.in/courses/106/104/106104128/
	Java : https://nptel.ac.in/courses/106/105/106105191/
	Evaluation of Textile materials : https://nptel.ac.in/courses/116/102/116102049/
To extract frames from a video:
	ffmpeg -i video.mp4 -vf fps=0.05 img/output%06d.png
To know more about how to custom train YOLOv3:
	https://towardsdatascience.com/training-yolo-for-object-detection-in-pytorch-with-your-custom-dataset-the-simple-way-1aa6f56cf7d9
	
	https://github.com/cfotache/pytorch_custom_yolo_training
