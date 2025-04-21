inputText = input("Enter text to write to the file: ")

try:
    outputFile = open("./Assignment4/file/output.txt", "w")
    outputFile.write(inputText)
    outputFile.write("\n")
    print("Data successfully written to output.txt.\n")
except FileNotFoundError:
    print("Error: The file 'output.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'outputFile' in locals():
        outputFile.close()

appendText = input("Enter additional text to append: ")

try:
    outputFile = open("./Assignment4/file/output.txt", "a")
    outputFile.write(appendText)
    outputFile.write("\n")
    print("Data successfully appended.\n")
except FileNotFoundError:
    print("Error: The file 'output.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'outputFile' in locals():
        outputFile.close()

try:
    outputFile = open("Assignment4/file/output.txt", "r")
    lines = outputFile.readlines()

    print("Final content of output.txt:")
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        print(lines[i])

except FileNotFoundError:
    print("Error: The file 'output.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'outputFile' in locals():
        outputFile.close()