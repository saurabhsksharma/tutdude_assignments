try:
    sampleFile = open("Assignment4/file/sample.txt", "r")
    lines = sampleFile.readlines()

    print("Reading file content:")
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        print(f"Line {i+1}: ", lines[i])

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'sampleFile' in locals():
        sampleFile.close()