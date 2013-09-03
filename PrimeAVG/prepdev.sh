#!/bin/bash

DEBDIR="${PWD%/*}/debpack"
BASEDIR=$PWD

MEDIASOURCE="${BASEDIR}/media"
DOCSOURCE="${BASEDIR}/doc"
SRCSOURCE="${BASEDIR}/src"


echo "\$DEBDIR is" $DEBDIR

echo "\$MEDIASOURCE is" $MEDIASOURCE
echo "\$SRCSOURCE is" $SRCSOURCE
echo "\$DOCSOURCE is" $DOCSOURCE

echo "Enter new avgui version"
read VERSION

echo "The new avgui version will be " $VERSION

for file in $DEBDIR/*
	do
		if [ -f $file ]; then
			rm -i $file
		elif [ -d $file ]; then
			for file2 in $file/*
			do
				if [ -d $file2 ]; then
					rm -r $file2
				fi
			done
			DESTINATION=${file%\-*}'-'$VERSION
			echo "Destination now is " $DESTINATION
			if [ $file != $DESTINATION ]; then				
				mv $file $DESTINATION
			fi
		fi

done 

MEDIADEST="${DESTINATION}/media"
DOCDEST="${DESTINATION}/doc"
SRCDEST="${DESTINATION}/src"

echo "Creating Media Destination dir..." $MEDIATEST
mkdir -p $MEDIADEST

echo "Creating Documents Destination dir..." $DOCDEST
mkdir -p $DOCDEST

echo "Creating Source Destination dir..." $SRCDEST
mkdir -p $SRCDEST

echo "Copying Media Files..."
for mediafile in $MEDIASOURCE/*
	do
		if [ -f $mediafile ]; then
			cp $mediafile $MEDIADEST/
		fi
done

echo "Copying Source Files..."
for srcfile in $SRCSOURCE/*
	do
		if [ -f $srcfile ] && [ ${srcfile#*.} != "sh" ] && [ ${srcfile#*.} != "sqlite" ]; then
			cp $srcfile $SRCDEST/
		fi
	done

echo "Copying Documentation Files..."
for docfile in $DOCSOURCE/*
	do
		if [ -f $docfile ]; then
			cp $docfile $DOCDEST/
		fi
done

echo "Done!"
