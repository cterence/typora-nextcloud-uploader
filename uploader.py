import sys
import os
import ntpath

import owncloud
from dotenv import load_dotenv


def main():
    load_dotenv()

    oc = owncloud.Client(os.getenv("DOMAIN"))
    oc.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))
    for arg in sys.argv[1:]:
        oc.put_file(f"{os.getenv('UPLOAD_DIRECTORY')}/{ntpath.basename(arg)}", arg)
        link = oc.share_file_with_link(
            f"{os.getenv('UPLOAD_DIRECTORY')}/{ntpath.basename(arg)}"
        )
        print(f"{link.get_link()}/preview")


if __name__ == "__main__":
    main()