file = (input("File name: ")).lower().strip()


if file.endswith((".jpg", ".jpeg")):
    print("image/jpeg" )
elif file.endswith(".gif"):
    print ("image/gif")
elif file.endswith("png"):
    print ("image/png")
elif file.endswith(".pdf"):
    print ("application/pdf")
elif file.endswith(".zip"):
    print ("application/zip")
elif file.endswith(".txt"):
    print ("text/plain")
else:
    print("application/octet-stream")

