init-dataset: clean download-dataset clean-dataset

download-dataset:
	wget -nc http://groups.csail.mit.edu/vision/LabelMe/NewImages/indoorCVPR_09.tar -P assets/
	tar xvf assets/indoorCVPR_09.tar -C assets/


clean-dataset:
	rm assets/Images/dining_room/salle-a-manger.JPG
	rm assets/Images/kindergarden/preschool-room.JPG
	rm assets/Images/kitchen/ISTOOL.JPG
	rm assets/Images/kitchen/KITCHEN4.JPG
	rm assets/Images/meeting_room/Meeting\ Room.JPG
	rm assets/Images/waitingroom/Waiting\ Room.JPG

	rm assets/Images/auditorium/auditorium986_120.jpg
	rm assets/Images/auditorium/auditorium776_118.jpg
	rm assets/Images/bar/bar_0075.jpg
	rm assets/Images/laundromat/Laundry_Room_bmp.jpg
	rm assets/Images/kindergarden/classroom_north_bmp.jpg
	rm assets/Images/waitingroom/Bistro_3_BMP.jpg

clean:
	rm -rf assets/Images