echo 'Benchmarking $(pwd)...' 
time (for i in {1..1000}; do echo $(pwd) > /dev/null; done) 
echo 'Benchmarking $PWD...' 
time (for i in {1..1000}; do echo $PWD > /dev/null; done)
