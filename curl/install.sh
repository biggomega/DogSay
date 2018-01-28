curl -sLo dogsay.tar.gz https://benbotvinick.com/projects/dogsay/dogsay.tar.gz
tar -xzpf dogsay.tar.gz
rm dogsay.tar.gz
mv dogsay/dogsay /usr/local/bin/dogsay
mv dogsay/dogsay.py /usr/local/bin/dogsay.py
rm -rf dogsay

