import sys
import os
import zlib



def init ():
    os.mkdir(".git")
    print("1")
    os.mkdir(".git/objects")
    print("2")
    os.mkdir(".git/refs")
    print("3")
    with open(".git/HEAD", "w") as f:
        print("1")
        f.write("ref: refs/heads/master\n")
    print("Initialized git directory")

def cat_file(blob_hash):
            
        hash = blob_hash

        dirname = hash[:2]

        filename = hash[2:]

        path = f".git/objects/{dirname}/{filename}"

        with open(path, "rb") as f:

            data = zlib.decompress(f.read()).split(b"\x00")[1]

            data = data.decode()

        print(data, end="")

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    #print("Logs from your program will appear here!")

    #
    command = sys.argv[1]
    if command == "init":
         init()
    elif command == "cat-file" and sys.argv[2] == "-p":
        blob_sha = sys.argv[3]
        cat_file(blob_sha)

    else:
         raise RuntimeError(f"Unknown command {command}")
    


if __name__ == "__main__":
    main()
