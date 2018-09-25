if [ $1 == 'server' ]
then
  cd server
  FLASK_APP=main.py flask run
elif [ $1 == 'web' ]
then
  npm run serve
elif [ $1 == 'build' ]
then
  npm run build
  tar czf dist.tar.gz dist
  mv dist.tar.gz ~/Desktop/
fi
