rm -rf /tmp/dogsay
rm /tmp/dogsay.tar.gz
rm /usr/local/bin/dogsay
rm /usr/local/bin/dogsay.py
curl -sLo /tmp/dogsay.tar.gz https://benbotvinick.com/projects/dogsay/dogsay.tar.gz
tar -xzpf /tmp/dogsay.tar.gz
rm /tmp/dogsay.tar.gz
mv /tmp/dogsay/dogsay /usr/local/bin/dogsay
mv /tmp/dogsay/dogsay.py /usr/local/bin/dogsay.py
rm -rf /tmp/dogsay

