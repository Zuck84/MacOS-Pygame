import os

print("")

jarvis = input("jarvis/MS-DOS> ")

if jarvis == "jarvis":
	print ("")
	os.system("python jarvis.py")

elif jarvis == "exit":
	print("End of the program...")

elif jarvis == "clear":
	os.system("cls")
	os.system("python jarvis.py")

elif jarvis == "about":
	print("")
	print("_______________JARVIS [1.0 version for MS-DOS]_______________")
	print("")
	print("")
	print("Just A Rather Very Intelligent System")
	print("Developed by Charles in October 2019.")
	print("It's the simplest command language made to replace CMD and BASH")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")


elif jarvis == "color":
	print("")
	print("Here are the choices: ")
	print("")
	print("dark blue")
	print("")
	print("green")
	print("")
	print("grey/blue")
	print("")
	print("")
	print("brown")
	print("")
	print("purple")
	print("")
	print("grey/green")
	print("")
	print("light grey")
	print("")
	print ("grey")
	print("")
	print("dark blue")
	print("")
	print("light green")
	print("")
	print("aqua")
	print("")
	print("red")
	print("")
	print("yellow")
	print("")
	print("white")
	print("")
	print("pink")
	print("")
	print("")
	print("Choose a color for...")
	os.system("python jarvis.py")


elif jarvis == "dark blue":
	os.system("color 1")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "green":
	os.system("color 2")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "grey/blue":
	os.system("color 3")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "brown":
	os.system ("color 4")
	print("")
	print("")
	print("")
	os.system("py jarvis.py")

elif jarvis == "purple":
	os.system("color 5")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "grey/green":
	os.system("color 6")
	print("")
	print("")
	print("")
	os.system("py jarvis.py")

elif jarvis == "light grey":
	os.system("color 7")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "grey":
	os.system("color 8")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "dark blue":
	os.system("color 9")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "light green":
	os.system("color A")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "aqua":
	os.system("color B")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "red":
	os.system("color C")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "yellow":
	os.system("color E")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "pink":
	os.system("color D")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "white":
	os.system("color F")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "pcname":
	os.system("hostname")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "ip":
	os.system("ipconfig")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "commands":
	print("")
	print("CLEAR = to clear the screen")
	print("")
	print("EXIT = to stop jarvis")
	print("")
	print("IP = to configure network")
	print("")
	print("COLOR = list of colors for jarvis")
	print("")
	print("PCNAME = to know your machine's name")
	print("")
	print("ABOUT = to know about the development of jarvis")
	print("")
	print("SAY = to make jarvis say something (press enter before typing what you want him to say")
	print("")
	print("PORT = to see opened ports")
	print("")
	print("SPEAK = to use JAI (Jarvis Artificial Intelligence) to help you.")
	print("")
	print("COMMANDS: to see the list of commands and the main rules to use Jarvis.")
	print("")
	print("TIME: change the time.")
	print("")
	print("DATE: change the date.")
	print("")
	print("PACKETS: send packets to a network host.")
	print("")
	print("BASIC: access to basic (cmd).")
	print("")
	print("LOOP: to test your RAM and your CPU by a loop with the size you want.")
	print("")
	print("INFINITY: to test your RAM and your CPU by an infinity size. (click on the cross to stop)")
	print("")
	print("DIRECTORY: list directory contents.")
	print("")
	print("NEWDIRECTORY: make a new directory (a file), rename it on your desktop")
	print("")
	print("REMOVEDIRECTORY: to remove a directory (please rename the directory/file you want to remove before you enter this command)")
	print("")
	print("TREE: to see your desktop tree.")
	print("")
	print("DESKTOP: to access to your desktop.")
	print("")
	print("SHUTDOWN: to shutdown your computer.")
	print("")
	print("REBOOT: to reboot your computer.")
	print("")
	print("REBOOTSOFTWARE: to reboot your computer and your softwares.")
	print("")
	print("SLEEP: Put the computer to sleep.")
	print("")
	print("GUI: to see your GUI (Graphical User Interface)")
	print("")
	print("RENAME: to rename a file.")
	print("")
	print("OSVERSION: to see your OS version")
	print("")
	print("ROUTINGTABLE: to print routing table.")
	print("")
	print("SERVICE: to start the service. (on Windows)")
	print("")
	print("SHAREDSERVICES: to see shared services.")
	print("")
	print("KNOCK KNOCK NEO: to launch the matrix...")
	print("")
	print("")
	print("")
	print("__________3 RULES TO RESPECT IF YOU WANT IT TO WORK__________")
	print("")
	print("1. PLEASE DO NOT USE CAPITAL LETTERS ONLY USE THE SMALL ONES.")
	print("")
	print("2. TO MAKE JARVIS SAY SOMETHING: TYPE SAY, PRESS ENTER, TYPE WHAT YOU WANT JARVIS TO SAY")
	print("")
	print("3.TO CHOOSE A COLOR YOU CAN WRITE THE NAME OF THE COLOR (PICK ONE FROM THE COLOR LIST OF JARVIS)")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "say":
	say = input("==> ")
	print("")
	print("Jarvis: ", "¨", say, "¨")
	os.system("python jarvis.py")

elif jarvis == "speak":
	os.system("cls")
	print("Hello new user. I am JAI (Jarvis Artificial Intelligence) and I was developed to help you in your tasks on the internet.")
	print("")
	print("But first of all I'd like to learn more about you.(all the informations will be saved until you close Jarvis)")
	print("")

	infoornot = input("Do you want JAI to call you by your name or not ? (yes or no) ==> ")

	if infoornot == "yes":
		firstname = input("First Name: ")
		lastname = input("Last Name: ")

	else:
		firstname = "#anonymous"
		lastname = "user"

	def aboutyouandmore():
		print("")
		print("")
		print("")
		print("Ok new user I will now remember your name is {} {} until you'll close JAI.".format(firstname, lastname))

	aboutyouandmore()

	def JAI():
		print("")
		print("[", firstname, lastname, "]")
		JAICS = input ("to JAI: ")

		if JAICS == "commands":
			print("")
			print("Here are the commands of JAI:")
			print("")
			print("")
			print("EXIT: to exit JAI and go back on the basic Jarvis")
			print("")
			print("GMAIL, HOTMAIL, YAHOOMAIL, INBOX, ICLOUD: to connect to your mail account (type one of these services name to access)")
			print("")
			print("ABOUTME: to see what JAI knows about you")
			print("")
			print("HELLO: say hello to JAI")
			print("")
			print("HEYGOOGLE: to go on google.")
			print("")
			print("WEBSITE: to go directly on a website from JAI")
			JAI()

		elif JAICS == "exit":
			os.system("python jarvis.py")

		elif JAICS == "gmail":
			os.system("start https://mail.google.com")
			JAI()

		elif JAICS == "hotmail":
			os.system("start https://outlook.live.com")
			JAI()

		elif JAICS == "yahoomail":
			os.system("start https://mail.yahoo.com")
			JAI()

		elif JAICS == "inbox":
			os.system("start www.inbox.com")
			JAI()

		elif JAICS == "icloud":
			os.system("start https://www.icloud.com")
			JAI()

		elif JAICS == "aboutme":
			def aboutyouandmore():
				print("")
				print("")
				print("")
				print("I know that your name is {} {}.".format(firstname, lastname))
			aboutyouandmore()
			JAI()

		elif JAICS == "clear":
			os.system("cls")
			JAI()

		elif JAICS == "hello":
			print("")
			print("Hello how can I help you", firstname, "? (enter a command)")
			JAI()

		elif JAICS == "heygoogle":
			os.system("start www.google.com")
			JAI()

		elif JAICS == "website":
			site=input("Which website ? (type NAMEOFTHEWEBSITE.com) ==> ")
			website = str("start www.{}".format(site))
			os.system(website)
			JAI()

		else:
			print("")
			print("")
			print("")
			print("Wrong Command")
			JAI()

	JAI()

elif jarvis == "port":
	os.system("netstat -a")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "date":
	os.system("date")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "time":
	os.system("time")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "packets":
	os.system("ping")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "basic":
	print("Here are the commands of MS-DOS CMD:")
	os.system("help")
	print("")
	os.system("cmd")

elif jarvis == "loop":
	loop = 0
	loop2 = input("loop size: ")
	loop2 = int (loop2)
	while loop < loop2:
		print("LOOP")
		loop += 1
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "infinity":
	loop = 3
	while loop < 5:
		print("testing your CPU and your RAM...")

elif jarvis == "directory":
	os.system("dir")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")

elif jarvis == "tree":
	os.system("tree")
	print("")
	print("")
	print("")
	os.system("python jarvis.py")


elif jarvis == "desktop":
	print("cd Desktop")

elif jarvis == "shutdown":
	os.system("shutdown /s")

elif jarvis == "reboot":
	os.system("shutdown /r")

elif jarvis == "rebootsoftware":
	os.system("shutdown /g")

elif jarvis == "sleep":
	os.system("shutdown /h")

elif jarvis == "gui":
	os.system("shutdown /i")
	os.system("python jarvis.py")

elif jarvis == "newdirectory":
	print("name of the new directory")
	newdir = input("==> ")
	os.system("mkdir {}".format(newdir))
	os.system("dir")
	os.system("python jarvis.py")

elif jarvis == "removedirectory":
	directoryname = input("name of the directory you want to delete: ")
	os.system("rmdir {}".format(directoryname))
	os.system("python jarvis.py")

elif jarvis == "rename":
	oldname = input ("name of the file: ")
	newname = input ("new name: ")
	rename = str("rename {} {}".format(oldname, newname))
	os.system(rename)
	os.system("python jarvis.py")

elif jarvis == "osversion":
	os.system("ver")
	os.system("python jarvis.py")

elif jarvis == "routingtable":
	os.system("route print")
	os.system("python jarvis.py")

elif jarvis == "service":
	os.system("net start")
	os.system("python jarvis.py")

elif jarvis == "sharedservices":
	os.system("net share")
	os.system("python jarvis.py")

elif jarvis == "knock knock neo":
	os.system("@echo off")
	os.system("color 0a")
	os.system(":top")

	hello = 3
	while hello < 5:
		os.system("echo %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random%")
		os.system("goto top")

else:
	print("")
	print("")
	print("")
	print("")
	print("Wrong Command")
	os.system("python jarvis.py")
