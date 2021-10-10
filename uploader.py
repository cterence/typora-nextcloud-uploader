import sys
import os
import ntpath
import owncloud
from dotenv import load_dotenv


def main():
    load_dotenv()
    oc = owncloud.Client(os.getenv("NC_URL"))
    oc.login(os.getenv("NC_USERNAME"), os.getenv("NC_PASSWORD"))
    for arg in sys.argv[1:]:
        oc.put_file(f"{os.getenv('NC_UPLOAD_DIRECTORY')}/{ntpath.basename(arg)}", arg)
        link = oc.share_file_with_link(
            f"{os.getenv('NC_UPLOAD_DIRECTORY')}/{ntpath.basename(arg)}"
        )
        print(f"{link.get_link()}/preview")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Usage: python3 uploader.py "/path/to/image1" "/path/to/image2" ...')
        sys.exit(1)
    else:
        main()
