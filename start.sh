echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/DKBOTx/MoosicPlayer /MoosicPlayer
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/DKBOTx/MoosicPlayer -b $BRANCH /MoosicPlayer
fi
cd /MoosicPlayer
pip3 install -U -r requirements.txt
echo "Starting Bot.... 𝙏𝙀𝙎𝙎𝘼"
python3 main.py
