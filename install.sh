curl -sOL https://benbotvinick.com/downloads/dogsay/dogsay.tar.gz
tar -xzpf dogsay.tar.gz
rm dogsay.tar.gz
sudo -kp "Please enter your password to install DogSay: " mv dogsay/dogsay /usr/bin/dogsay
mv dogsay/ ~/.dogsay/
tput setaf 2
tput bold
echo "Success!"
tput sgr0
