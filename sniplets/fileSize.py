old_file_position = fileOut.tell()

    # Moving the file handle to the end of the file
    fileOut.seek(0, 2)

    # calculates the bytes 
    size = fileOut.tell()
    print('file size is', size, 'bytes')
    fileOut.seek(old_file_position, 0)

    fileOut.close




    stats = os.stat(nameOut)