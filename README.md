# One-way-sincronization

For each of the folders I have created a separate class with its operations.
The Source class firstly checks if the path directed from input exists or not and the other operation returns a dictionary with key values the files' names inside the source folder and as value the file content.
The Replica class also determines whether the path directed by input is present or not. When there are no files in the source folder, it removes all of the files from the replica folder, and when there are files, it generates the files using the dictionary obtained from the Source class.
The log output file is automatically created after you give the name from input.
To run the program simply run the main.py file (ex. python3 main.py)
