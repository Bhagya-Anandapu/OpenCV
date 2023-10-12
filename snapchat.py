import cv2
import os

userID = {}
currentUSR = ""

def signUp():
    user = input("Enter username: ")
    psd = input("Enter password: ")
    p = input("Re-enter password: ")
    while psd != p:
        print("Passwords do not match. Retry!!")
        psd = input("Enter password: ")
        p = input("Re-enter password: ")
    parent_dir = os.getcwd()
    
    # Create the 'coding' directory if it doesn't exist
    os.makedirs(parent_dir, exist_ok=True)
    
    path = os.path.join(parent_dir, user)
    try:
        os.mkdir(path)
        print("Directory '%s' created" % user)
    except FileExistsError:
        print("Directory '%s' already exists" % user)
    userID[user] = psd
    print(userID)

# ... rest of your code ...


def snap():
    
    output_directory = os.path.join(os.getcwd(), currentUSR)  # Use the current working directory

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)  # Create the directory if it doesn't exist

    cam = cv2.VideoCapture(0)
    cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)

    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow("press space to take a photo", frame)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            nam=input("Enter image name:")
            img_name = os.path.join(output_directory, nam+".jpg".format(img_counter))
            if cv2.imwrite(img_name, frame):
                print("{} written!".format(img_name))
                img_counter += 1
            else:
                print("Failed to write image.")
    cam.release()
    cv2.destroyAllWindows()

def quit_program():
    global currentUSR
    currentUSR = ""
    exit()

def view():
    global currentUSR
    folder_path = "C:/Users/yaswanth kumar/OneDrive/Desktop/coding/"+currentUSR
    files = os.listdir(folder_path)

# Iterate over the files and print their names
    for file in files:
        print(file)
    image_name = input("Enter image name: ")+".jpg"  # Change to the name of your image file

    # Construct the full path to the image file
    image_path = os.path.join(folder_path, image_name)

    # Check if the image file exists
    if os.path.isfile(image_path):
        # Read the image using OpenCV
        image = cv2.imread(image_path)

        if image is not None:
            # Display the image
            cv2.imshow("Image Viewer", image)

            # Wait for a key press and close the window
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Failed to read the image.")
    else:
        print(f"Image '{image_name}' not found in the folder.")


def signIn():
    global currentUSR
    user = input("Enter user ID: ")
    if user in userID:
        psd = input("Enter password: ")
        if psd == userID[user]:
            currentUSR = user
            print("1.Take a picture")
            print("2.View image")
            print("3.Logout")
            choice = input("Enter choice: ")
            if choice=='3':
                quit_program()
            elif choice=='1':
                snap()            
            elif choice=='2':
                view()
            
        else:
            print("Incorrect password.")
            signIn()

def Options():
    print("1. Sign In")
    print("2. Sign Up")
    print("3. Quit")
    choice = input("Enter choice: ")
    if choice == '1':
        signIn()
        Options()
    elif choice == '2':
        signUp()
        Options()
    elif choice == '3':
        quit_program()
    else:
        print("Invalid choice. Please try again.")
        Options()

Options()
