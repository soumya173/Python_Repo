import os,shutil

dir_paths = [r'C:\Windows\Temp', r'C:\Users\sgorai\AppData\Local\Temp']

for dir_path in dir_paths:	

	for f in os.listdir(dir_path):
		print("Current Directopry: " + dir_path)
		complete_path = dir_path + "\\" + f
		try:			
			if os.path.isfile(complete_path):
				os.remove(complete_path)			
			elif os.path.isdir(complete_path) :
				shutil.rmtree(complete_path, ignore_errors=True)

			print("Removed: " + f)
		except Exception as e:
			print("Failed to remove: " + f)
			print("Reason: " + str(e))
			
