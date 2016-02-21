#!/bin/sh
	ADB()
		{     
			echo Ready to use ADB commands.
			echo
			echo Showing currently connected ADB devices. Serial number first, status.
			adb devices
			echo
			adb get-serialno
			$serialno
			echo "$serialno"
			adb pull "$inputDir" "$outputDir"
			echo
			echo Pulled from the input Directory "$inputDir" and pushed to the output Directory "$outputDir".
					}
	echo Start Android2PC program
	#echo "postitional parameters"
	#echo '$1 = ' $1
	#echo '$2 = ' $2
	#echo '$3 = ' $3
	#echo '$4 = ' $4
	echo i INPUT
	echo o OUTPUT
	echo a ADB
	if [ "$#" = 4 ]; then

		if [ "$1" = "-i" ]; then
		   inputDir=$2
		fi
		if [ "$3" = "-o" ]; then
		   outputDir=$4
		fi
		
		ADB 
		
		echo New input directory is $inputDir
		mkdir $outputDir    
		echo New output directory is $outputDir
		echo Program complete, exit command line
	fi
	exit 0