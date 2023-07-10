#!/usr/bin/python3

'''
Aim - to create a class that will build a playlist file, or play a playlist file.

Put code for checking if file exists in the   name == main   section at the end of this file.
'''



class PlaylistFinishedError(Exception):
	pass

class playerV2:
	#def __init__(self):
	#	what here?

	def generate_playlist(self, dir=".", exts=[".mp3", ".MP3"], playlist_name="playlist_file.txt"):
		import os

		self.playlist_name = playlist_name
		self.clean_playlist = []
		self.fancy_playlist = []
		self.listdir_list = os.listdir(dir)
		self.listdir_list.sort(key=lambda s: s.casefold())
		for item in self.listdir_list:
#			print(item + " " + str((item[-4:] in exts)))
			if item[-4:] in exts:
				self.clean_playlist.append(item)

		for clean_item in self.clean_playlist:
#			print(":-: " + item)
			self.fancy_playlist.append(":-: " + clean_item + "\n")

		if dir[-1] == ("/" or "\\"):
			clean_dir = dir
		elif dir[-1] != ("/" or "\\"):
			clean_dir = str(dir + "/")

		with open(clean_dir+self.playlist_name, "w") as playlist_file:
			for fancy_item in self.fancy_playlist:
				playlist_file.write(str(fancy_item))

#		print(self.listdir_list)
#		print(self.clean_playlist)
		#print(self.fancy_playlist)

	def play_playlist(self, dir=".", playlist_name="playlist_file.txt", shuffle=False):
		import os.path

		if dir[-1] == ("/" or "\\"):
			clean_dir = dir
		elif dir[-1] != ("/" or "\\"):
			clean_dir = str(dir + "/")


		if playlist_name_exists := os.path.isfile(clean_dir + playlist_name):
			import playsound
			#import time
			#from mutagen.mp3 import MP3
			#import subprocess
		elif playlist_name_exists == False:
			raise FileNotFoundError(f"File \"{playlist_name}\" not found.")
			input("\nPress enter to contine...")
			exit()

		with open(clean_dir+playlist_name, "r") as playlist_file:
			read_playlist = playlist_file.read()
#		print(read_playlist)
		sanitized_playlist = read_playlist.split("\n")

		played_items = []
		unplayed_items = []
		unplayed_items_to_write = []

		for item in sanitized_playlist:
			if item[0:3] == ":-:":
				unplayed_items.append(item)
				unplayed_items_to_write.append(item)
			elif item[0:3] == ":#:":
				played_items.append(item)
			elif item[0:3] == ":X:":
				raise PlaylistFinishedError(f"Playlist finished. Please delete the file \"{playlist_name}\" and generate a new playlist.")
				exit()

		'''
		try:
			sanitized_playlist.remove("")
		except:
			pass
		'''

#		print(sanitized_playlist)

#		if shuffle:
#			import random
#			random.shuffle(sanitized_playlist)

		if shuffle:
			import random
			random.shuffle(unplayed_items)

#		print(sanitized_playlist)

		to_write = []

		#import time
		for item in unplayed_items:
			print(f"Playing {item[4:]}")
			#print(played_items, unplayed_items, "\n")

			played_items.append(item.replace(":-:", ":#:"))
			unplayed_items_to_write.remove(item)
			#print(played_items, unplayed_items_to_write, "\n")
			#time.sleep(3)
			playsound.playsound(clean_dir+item[4:])

			temp_playlist = played_items + unplayed_items_to_write
			#temp_playlist.remove("")

			with open(clean_dir+playlist_name, "w") as playlist_file:
				for item in temp_playlist:
					playlist_file.write(item + "\n")



#		for item in sanitized_playlist:
#			if item[0:3] == ":X:":
#				#print(f"Playlist finished. Please delete the file \"{playlist_name}\" and generate a new playlist.")
#				#input("\nPress enter to contine...")
#				raise PlaylistFinishedError(f"Playlist finished. Please delete the file \"{playlist_name}\" and generate a new playlist.")
#				exit()
#			elif item[0:3] == ":#:":
#				print(f"Played {item[4:]}. Skipping...")
#				to_write = [sanitized_playlist.index(item), item]
#			elif item[0:3] == ":-:":
#				print(f"Playing {item[4:]}")
#				playsound.playsound(clean_dir+item[4:], block=True)
#
#				#playsound.playsound(item[4:], block=False)
#				#time.sleep((MP3(item[4:]).info.length) + 1)
#				to_write = [sanitized_playlist.index(item), item.replace(":-:", ":#:")]
#
#			with open(clean_dir+playlist_name, "r") as temp_playlist_file:
#				temp_playlist = temp_playlist_file.read().split("\n")
#
#			#print(temp_playlist)
#
#			#print(temp_playlist[to_write[0]])
#			del temp_playlist[to_write[0]]
#			temp_playlist.insert(to_write[0], to_write[1])
#
#			#print(temp_playlist)
#
#			temp_playlist.remove("")
#
#			with open(clean_dir+playlist_name, "w") as playlist_file:
#				for item in temp_playlist:
#					playlist_file.write(item + "\n")



#		print(sanitized_playlist)

		with open(clean_dir+playlist_name, "w") as playlist_file:
			playlist_file.write(":X:")
		#print(f"Playlist finished. Please delete the file \"{playlist_name}\" and generate a new playlist.")
		#input("\nPress enter to contine...")
		raise PlaylistFinishedError(f"Playlist finished. Please delete the file \"{playlist_name}\" and generate a new playlist.")





if __name__ == "__main__":
	import os

	player = playerV2()

	'''
	#player.generate_playlist(dir="./wav", exts=[".wav"], playlist_name="wavs")
	#player.generate_playlist()
	#os.system(f"cat {player.playlist_name}")

	#player.play_playlist()
	#player.play_playlist(dir="./wav", playlist_name="wavs")
	#player.play_playlist(playlist_name="./wav/wavs")
	#player.play_playlist(shuffle=True)
	#player.play_playlist(shuffle=True, playlist_name="done_list")
	#player.play_playlist(shuffle=True, playlist_name="efgviurthrt")
	'''

	import sys
	del sys.argv[0]

	help_message = '''pfolder2.py [-d=DIRECTORY|--directory=DIRECTORY] GENERATE|PLAYLIST [-s|--shuffle]

Where GENERATE take the form:
	-g=PLAYLIST | --generate=PLAYLIST

	and generates a playlist under the filename PLAYLIST in directory DIRECTORY

and PLAYLIST takes the form
	-p=PLAYLIST | --playlist=PLAYLIST

	and plays playlist under filname PLAYLIST in directory DIRECTORY, shuffling \n\tthe order of songs based on whether -s or --shuffle is passed at the command line

'''
	working_dir = "."
	listname = "playlist_file.txt"
	shuffle_arg = False
	action = ""

	for arg in sys.argv:
		if arg == "-h" or arg == "--help":
			print(help_message)
		elif arg[0:2] == "-d" or arg[0:11] == "--directory":
			if "=" in arg:
				working_dir = arg[arg.index("=")+1:]
			elif "=" not in arg:
				print("No working directory specified. Defaulting to \".\"...")
		elif arg[0:2] == "-p" or arg[0:10] == "--playlist":
			action = "play"
			if "=" in arg:
				listname = arg[arg.index("=")+1:]
			elif "=" not in arg:
				print("No playlist name specified. Defaulting to \"playlist_file.txt\"...")
		elif arg == "-s" or arg == "--shuffle":
			shuffle_arg = True
		elif arg == "-g" or arg == "--generate":
			action = "generate"
			if "=" in arg:
				listname = arg[arg.index("=")+1:]
			elif "=" not in arg:
				print("No playlist name specified. Defaulting to \"playlist_file.txt\"...")
		else:
			print(f"Unrecognized option {arg}. Use \"-h\" or \"--help\" to display a handy-dandy help dialogue.")

	#print(f"Working directory: \"{working_dir}\"")
	#print(f"Playlist name: \"{listname}\"")
	#print(f"Shuffle: {shuffle_arg}")


	if action == "":
		print("Please either generate or play a playlist.")
	elif action ==  "generate":
		player.generate_playlist(dir=working_dir, playlist_name=listname)
	elif action == "play":
		player.play_playlist(dir=working_dir, playlist_name=listname, shuffle=shuffle_arg)
