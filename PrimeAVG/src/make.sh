#!/bin/bash

RESFILE=avg.qrc

#checking integrity of resource file
#every .png file within the media directory should have its own entry in the resource file
cd ${AVGPR}/media
echo "Changed to " $PWD
echo "Assuming resource file name is " $RESFILE

if [ ! -f $RESFILE ]; then
	echo "Resource file does not exist, will create one..."
	echo "<!DOCTYPE RCC><RCC version=\"1.0\">" 	>> $RESFILE
	echo "<qresource>"  				>> $RESFILE
	echo "</qresource>" 				>> $RESFILE
	echo "</RCC>"	  				>> $RESFILE
fi

for file in $(ls $PWD)
do

	if [ "${file##*.}" == "png"  ]; then
		echo "Found a .png file: " $file
		result=$(grep $file $RESFILE | wc -l)
		#echo $result
		if [ $result == 0 ]; then
			#echo $file
			toInsert="<file>$file</file>"
			#echo "toInsert variable: " $toInsert
			LINNO=$(( $LINNO + 1))
			#echo "LINNO is : " $LINNO
			sed  --in-place -r "3i \\\t $toInsert" $RESFILE 		
		fi
	fi
done

cat $RESFILE

echo "Removing previous .py resource file and creating a new one.."
RESFILEPY=${RESFILE%.*}_rc.py
if [ -f $RESFILEPY ]; then
	rm $RESFILEPY
fi

pyside-rcc -py3 $RESFILE -o $RESFILEPY
echo "Moving the .py resource file to src folder"
mv $RESFILEPY ${AVGPR}/src

echo "preparing the .ui files - compiling them to .py"
cd ${AVGPR}/ui
echo "Changed to " $PWD
echo "Compiling .ui files..."
for file in $(ls $PWD)
do
	if [ "${file##*.}" == "ui"  ]; then
		echo "Found a .ui file: " $file
		PYFILEUI=${file%.*}UI.py
		pyside-uic $file -o $PYFILEUI
		mv $PYFILEUI ${AVGPR}/src
	fi
done
