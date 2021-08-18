counter=1
while [ $counter -le 10 ]
do
vcgencmd measure_temp
((counter++))
done
