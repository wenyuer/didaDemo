if [ $1 == 'server' ]
then
  cd server
  FLASK_APP=main.py flask run
elif [ $1 == 'web' ]
then
  npm run serve
fi
