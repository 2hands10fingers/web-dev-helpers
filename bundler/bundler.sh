#Bash script found in the pash profile to atuomate this bundler to locate bundle.js and wrap it.

bundler () {
  echo "Wrapping a bundle is redundant, but we gotta do it anyways"
  python ~/bundler.py -w ~/$1/wordpress/wp-content/themes/$1/assets/bundle.js
  open -R ~/$1/wordpress/wp-content/themes/$1/assets/bundle.js
  echo "Wrapping complete, yo."
}
