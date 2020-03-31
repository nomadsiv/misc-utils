import os
from optparse import OptionParser

from pdf2image import convert_from_path


def batch_convert_pdf_to_jpg(pdf_path):
    # TODO implement dir walk and for loop to call the convert function
    pass


def convert_pdf_to_jpg(pdf_file):
    pdf_file_without_path = os.path.basename(pdf_file)
    pdf_name, extn = pdf_file_without_path.split(".")

    pages = convert_from_path(pdf_file, 500)

    idx = 0
    for page in pages:
        idx += 1
        if len(pages) == 1:
            jpg_name = "{}.jpg".format(pdf_name)
        else:
            num_zero_padding = 2 if len(pages < 100) else 4
            zidx = idx.zfill(num_zero_padding)
            jpg_name = "{}-p-{}.jpg".format(pdf_name, zidx)

        page.save(jpg_name)


def _usage():
    print("Usage:")
    print("python3 pdf-to-jpg.py [-d] <pdf file full path>")
    print("If -d is specified, the path is treated as a folder and all pdfs in the folder are converted to jpgs")
    exit(1)


if __name__ == "__main__":

    """
        # prereq: poppler (a stand-alone util which is wrapped by python library pdf2image)
        # poppler for Windows Subsystem Linux:
        sudo apt install poppler-utils
        
        poppler for windows:
        https://stackoverflow.com/questions/18381713/how-to-install-poppler-on-windows
        http://blog.alivate.com.au/poppler-windows/

        # pip install pdf2image (do within a virtual env for best hygiene)

        this script reads either:
        - a pdf file from the given path and converts it to jpg
        - a directory containing pdf's and converts each pdf in the dir to jpg
        if there is a single page in the pdf, the script gives the same name to the jpg as the original pdf.
        for multi-page pdf's, it appends -p-<page-number> to the original pdf name for each of the jpgs.
    """

    parser = OptionParser()
    (options, args) = parser.parse_args()
    print("Got options: ", options)
    print("Got input args: ", args)
    if not len(args) == 1:
        _usage()

    print("Got input expense file args[0]: ", args[0])
    # print("Got input expense file args[1]: ", args[1])

    pdf_file_full_path = args[0]

    # TODO fix option parsing properly
    if (options == "d"):
        batch_convert_pdf_to_jpg(pdf_path)
    else: # single file
        convert_pdf_to_jpg(pdf_file_full_path)

