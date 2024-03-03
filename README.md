# processing-text
processing text based on allowed chars\
there are three separate programs:
1. delete chars- delete chars that are not in the hebrew and english alphabet and not : '"' , ':' , ',' , ':' , '.'
2. reverse text and delete chars- delete chars and reverse the words in each line + reverse letters in each hebrew word\
the programs receive a txt file in arg e.g. 'yourfile.txt' and output in the same location 1.'yourfile filterd.txt' 2. 'yourfile reversed'.txt\
3.process_files_gui- GUI interface that gives options to the user on what process he wants to do with the file:
	a. delete chars that are not in the  english alphabet reverse words in each line and reverse characters in each Hebrew word
	b. delete chars that are not in the  hebrew alphabet
	c delete chars that are not: '"' , ':' , ',' , ':' , '.'
	d. create an entry for custom allowed character
	e.reverse the words in each line + reverse letters in each hebrew word
	input by selecting a txt file output by selecting output location

##coming up:
1. fix bugs in process_files_gui:
	a. process file even if there is no selection 

2. new features:
 a. selecting a PDF file and extracting text from it
 b. add a function that in the done pop-up message the user can open the new file
 c. giving the output file a default name based on the selected process
