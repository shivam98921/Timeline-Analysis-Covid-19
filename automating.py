import pyautogui
import time

pyautogui.FAILSAFE = True
location = "D:\Python\\automation\\"
automate = False


def automate_cont():
    try:
        print("Checking for Unread Messages...")
        r = locate_img('whatsapp\\unread_msg.png',10,.8)
        print("A new message found...Forwarding it.")
        find_class((410,r[1],950,570))
    except KeyboardInterrupt:
        main()

def locate_img(img,tm=1,confidnc=1):
    r = None
    while r == None:
        r = pyautogui.locateCenterOnScreen(location+img,grayscale="True",confidence=confidnc)
        time.sleep(tm)
    return r

def locate_img_time(img,tm=3,confidnc=1,chk=3):
	r=None
	while chk != 0:
		r = pyautogui.locateCenterOnScreen(location+img,grayscale="True",confidence=confidnc)
		if r != None:
			break
		time.sleep(tm)
		chk -= 1
	return r

def set_google_meeting():
    print("Setting up a Google Meeting. Wait...")
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.typewrite(['c','h','r','o','m','e','space','m','e','e','t','.','g','o','o','g','l','e','.','c','o','m','enter'],interval=.3)
    time.sleep(10)
    # webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open_new_tab('google.com')
    print("Searching New Meeting Button...")
    pyautogui.moveTo(locate_img('gmeet\\gmeet_new_meeting.png',1,.5))
    pyautogui.click()
    print("Starting an instant meeting...")
    pyautogui.moveTo(locate_img('gmeet\\start_gmeet_meeting.png',1,.7))
    pyautogui.click()
    time.sleep(10)
    print("Joining Meeting...")
    pyautogui.moveTo(locate_img('gmeet\\gmeet_join_meeting.png',1,.8))
    pyautogui.click()
    time.sleep(5)
    print("Copying joining info...")
    pyautogui.moveTo(locate_img('gmeet\\copy_joining_info.png',1,.5))
    pyautogui.click()
    print("Opening Whatsapp...")
    time.sleep(1)
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.typewrite(['w','h','enter'],interval=.3)
    print("Sending link to Shivam Prajapati...")
    pyautogui.moveTo(locate_img('contacts\\shivam_prajapati.png',3,.8))
    # pyautogui.moveTo(locate_img('contacts\\ashmit_mittal.png',3,.8))
    pyautogui.click()
    pyautogui.hotkey('ctrl','v')
    pyautogui.typewrite(['enter'])
    pyautogui.hotkey('alt','tab')
    print("You are Ready to roll...")
    pyautogui.moveTo(locate_img('gmeet\\cross.png',1,.8))
    pyautogui.click()

def refresh():
	i=0
	print("Refreshing...")
	while i <3:
		pyautogui.moveTo(680,330)
		pyautogui.click(button='right')
		pyautogui.moveRel(30,55)
		time.sleep(1)
		pyautogui.click()
		i+=1

def open_cse_grp():
    print("Opening CSE group...")
    pyautogui.moveTo(locate_img('contacts\\cse_group.png',1,.5))
    # pyautogui.moveTo(locate_img('contacts\\ashmit_mittal.png',1,.5))
    pyautogui.click()
    pyautogui.moveTo(700,500)

def setup_college():
    print("Opening whatsapp...")
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.typewrite(['w','h','enter'],interval=.7)
    # time.sleep(20)
    # webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open_new_tab('https://www.notion.so/7f89acf8e56f4325bfec9f7d23fc5ed5?v=b7a104e534f8404fa78fdb8557007378')
    time.sleep(15)
    # #For Notion
    # r = None
    # num_time = 3
    # print("Seperating notion and whatsapp...")
    # while num_time != 0:
    #     time.sleep(3)
    #     r = pyautogui.locateCenterOnScreen(location+'notion\\notion.png')
    #     if r != None:
    #         break
    #     num_time -= 1
    # if r != None:
    #     pyautogui.moveTo(500,20)
    #     pyautogui.dragTo(2000, 0, duration=2)
    open_cse_grp()
    find_class()

def schedule_class(r):
    class_timing = pyautogui.prompt('In how many minutes, do you want to join the meeting?')
    print("Okay, Waiting for "+str(class_timing)+" minutes..")
    time.sleep(60*(int(class_timing)-1))
    print("It's about time to join the meeting... 1 minute left.")
    time.sleep(30)
    print("Joining meeting in 10 seconds...Don't move the mouse.")
    time.sleep(10)
    pyautogui.moveTo(r)
    join()

    

def forward_msg():
    # time.sleep(10)
    print("Opening menu...")
    pyautogui.moveTo(locate_img('whatsapp\\arrow.png',1,.9))
    pyautogui.click()
    print("Clicking on Forward Button...")
    pyautogui.moveTo(locate_img('whatsapp\\forward.png',1,.85))
    pyautogui.click()
    pyautogui.moveTo(locate_img('whatsapp\\forward_arrow.png',1,.9))
    pyautogui.click()
    print("Searching Contact...")
    time.sleep(1)
    pyautogui.typewrite("nav",interval=.9)
    pyautogui.moveTo(locate_img('whatsapp\\checkbox.png',1,.9))
    pyautogui.click()
    pyautogui.moveTo(locate_img('whatsapp\\send.png',1,.9))
    print("Sending Message...")
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)
    open_cse_grp()
    global automate
    if automate:
        automate_cont()

def join_gmeet():
    print("Place your mouse over the meeting link in 5 seconds...")
    time.sleep(5)
    pyautogui.click()
    time.sleep(10)
    print("Turning your video and Mic off...")
    pyautogui.click(locate_img('gmeet\\video.png',2,.8))
    pyautogui.click(locate_img('gmeet\\mic.png',2,.8))
    print("Asking to join the meeting...")
    pyautogui.moveTo(locate_img('gmeet\\ask_join.png',1,.7))
    pyautogui.click()
    print("You are in the meeting now.")


def join():
	pyautogui.click()
	time.sleep(15)
	pyautogui.click(locate_img_time('zoom\\without_video.png',2,.7))
	locate_img('zoom\\waiting_room.png',1,.7)
	print("You are in the waiting room...")
	r = 2
	while r!= None:
		r = pyautogui.locateCenterOnScreen(location+'zoom\\test_computer_audio.png',grayscale=True,confidence=.8)
		print("Waiting for the Teacher to let you in...")
		time.sleep(1)
	print("You are in the meeting now...")
	chk = 3
	print("Checking Microphone if it is muted or not.")
	r = locate_img_time('zoom\\mute.png',3,.7,8)
	if r != None:
		print("Your Mic is open. Stay silent. Turning your mic off...")
		pyautogui.moveTo(r)
		pyautogui.click()
		print("Your Mic is muted now.")
	else:
		print("Looks like your mic is muted. Check again to verify. Press ALT to show or hide meeting controls.")
	
def find_class(region=(410,95,950,570)):
	r=[]
	d=[]
	print("Checking for Classes",end="")
	while r == [] and d == []:
		print(".",end="")
		r = list(pyautogui.locateAllOnScreen(location+'zoom\class.png', grayscale=True, confidence=.72, region=region))
		d = list(pyautogui.locateAllOnScreen(location+'zoom\\daa.png',grayscale=True,confidence=.6, region=region))
		print(r)
		print(d)
		print(".")
		time.sleep(1)
	if r == []:
		for pos in d:
			coordinates = pyautogui.center(pos)
			class_found(coordinates,False)
	else:
		for pos in r:
			coordinates = pyautogui.center(pos)
			class_found(coordinates,True)
	
		
def class_found(coordinates,r):
    print("Found a class at the current mouse position")
    pyautogui.moveTo(coordinates)
    global automate
    if automate:
        choice = "Forward Message"
    else:
        choice = pyautogui.confirm(text='Class Found.', title='Found a Class at the current mouse position', buttons=['Forward Message', 'Join Class','Schedule Class','Check Next'])
    if choice == 'Forward Message':
        pyautogui.moveTo(coordinates)
        print("Forwarding Message...")
        forward_msg()
    elif choice == 'Join Class':
        pyautogui.moveTo(coordinates)
        if r:
            pyautogui.moveRel(-110,120)
        else:
            pyautogui.moveRel(-10,10)
        print("Joining the Class. Please Wait...")
        join()
    elif choice == 'Schedule Class':
        if r:
            schedule_class((coordinates[0]-110,coordinates[1]+120))
        else:
            schedule_class((coordinates[0]-10,coordinates[1]+10))
    elif choice == 'Check Next':
        return


def main():
    choice = pyautogui.confirm('Option',buttons=['Setup for College','Check for classes','Automate','Refresh','Setup a G-meeting','Forward Msg','Join G-mmet'])
    if choice == 'Check for classes':
        find_class()
    elif choice == 'Refresh':
        refresh()
    elif choice == 'Setup a G-meeting':
        set_google_meeting()
    elif choice == 'Setup for College':
        setup_college()
    elif choice == 'Forward Msg':
        print("Place your mouse over the message to be forwareded in 5 seconds.")
        time.sleep(5)
        forward_msg()
    elif choice == 'Join G-mmet':
        join_gmeet()
    elif choice == 'Automate':
        global automate
        automate = True
        automate_cont()
    if choice != None:
        print("Done. What Next?")
        main()

try:
    main()
except KeyboardInterrupt:
    print("Thank You for using me.")
