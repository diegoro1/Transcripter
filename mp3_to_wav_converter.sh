for FILE in *.mp3; 
do 
    name=$(basename "$FILE" .mp3)
    echo "converting $FILE to $name.wav" 
    afconvert -d LEI16 -f 'WAVE' $FILE "$name.wav"; 
done 
