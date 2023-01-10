#!/usr/bin/python3
""" module defines append_after method """


def append_after(filename="", search_string="", new_string=""):
    """
       inserts a line of text to a file, after each line
       containing a specific string
       args:
           filename: file to write to
           search_string: search string to begin append
           new_string: appended string
    """
    with open(filename, mode="r+", encoding="utf-8") as fr:
        file_read = ""
        for line in fr:
            file_read += line
            if search_string in line:
                file_read += new_string
    with open(filename, mode="w", encoding="utf-8") as fw:
        fw.write(file_read)
