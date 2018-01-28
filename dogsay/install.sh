rm -rf /private/tmp/dogsay
rm -f /private/tmp/dogsay.tar.gz
rm -f /usr/local/bin/dogsay
rm -f /usr/local/bin/dogsay.py
curl -sLo /private/tmp/dogsay.tar.gz https://benbotvinick.com/projects/dogsay/dogsay.tar.gz
tar -xzpf /private/tmp/dogsay.tar.gz
rm /private/tmp/dogsay.tar.gz
mv /private/tmp/dogsay/dogsay /usr/local/bin/dogsay
mv /private/tmp/dogsay/dogsay.py /usr/local/bin/dogsay.py
rm -rf /private/tmp/dogsay

