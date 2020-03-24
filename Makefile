.PHONY: run

run:
	#+=====================================+
	#|         BG INSTALLING KIVY          |
	#+=====================================+
	python3 setup.py

	#+========================+
	#|    STARTING X11 VNC    |
	#+========================+
	polygott-x11-vnc

	#+========================+
	#|    RUNNING PYTHON3     |
	#+========================+
	DISPLAY=:0 python3 test_kivy_1.py
