# processing-text
processing text based on allowed chars
there are three separate programs:
1. delete chars- delete chars that are not in the Hebrew and English alphabet and not : '"' , ':' , ',' , ':' , '.'
2. reverse text and delete chars- delete chars and reverse the words in each line + reverse letters in each Hebrew word\
the programs receive a txt file in arg e.g. 'yourfile.txt' and output in the same location 1.'yourfile filterd.txt' 2. 'yourfile reversed'.txt\
3.process_files_gui- GUI interface that gives options to the user on what process he wants to do with the file:
	a. delete chars that are not in the English alphabet reverse words in each line and reverse characters in each Hebrew word
	b. delete chars that are not in the Hebrew alphabet
	c delete chars that are not: '"' , ':' , ',' , ':' , '.'
	d. create an entry for custom custom-allowed character
	e.reverse the words in each line + reverse letters in each Hebrew word
	input by selecting a txt file output by selecting output location

## Whats new:
1. fix bugs in process_files_gui:
	a. process file even if there is no selection-V 

2. new features:
	a. add a function that in the done pop-up message the user can open the new file-V
	b. giving the output file a default name based on the selected process-V

3. building foundation for:
	comingup.2.a&b

##coming up:
1. fix bugs in process_files_gui:
2. new features:
 	a. adding multiple files  support
 	b. maybe changing it to more OOP
 	c. selecting a PDF file and extracting text from it
