#!/usr/bin/sh

env_loc="${HOME}/enhance_envs";

###############################################################################

function error() {
  local msg="$1"
  echo "ERROR: $msg"
}

###############################################################################

function warning() {
  local msg="$1"
  echo "WARNING: $msg"
}

###############################################################################

function get_pdir() {
  local name="$1";
  local pdir="$env_loc/$name/"
  echo "$pdir"
}

###############################################################################

function new_env() {
  if [ "${INSIDEENHANCEENV}" == "YES" ]; then
    warning "Already inside env ${CURRENTENHANCEENV}"
  fi
  
  name="$1";
  pdir=`get_pdir $name`

  if [ -e "$pdir" ]; then
    error "This environment already exists"
    exit 1;
  fi

  git clone git@github.com:thiesgehrmann/enhance.git $pdir;
  mkdir $pdir/root
  cd $pdir/root && $pdir/enhance init generic  
  gen_env_vars "$name" > $pdir/env
}

###############################################################################

function gen_env_vars() {
  name="$1"
  pdir=`get_pdir $name`
  ENHANCEHOME="$pdir"
  echo "export INSIDEENHANCEENV=YES"
  echo "export CURRENTENHANCEENV=$name"
  echo "export ENHANCEHOME=$pdir"
}

###############################################################################

function cat_env_vars() {
  name="$1"
  pdir=`get_pdir $name`
  cat $pdir/env
}

###############################################################################

function del_env(){

  name="$1";
  pdir=`get_pdir $name`
  rm -rf $pdir

}

###############################################################################

function list_envs() {
  ls $brew_loc
}

###############################################################################

function enter_env() {
  if [ "${INSIDEENHANCEENV}" == "YES" ]; then
    error "Already inside env ${CURRENTENHANCEENV}"
    exit 1
  fi

  name="$1";
  pdir=`get_pdir $name`

  if [ ! -e "$pdir" ]; then
    error "Env $name does not exist";
    exit 1
  fi

  source "${pdir}/env"
  source "${pdir}/root/paths"
  echo "Entering Enhance env: $name"
  exec $SHELL
  echo "Exiting Enhance env: $name"
}

###############################################################################

action="$1";
name="$2";

case $action in
  n)
   new_env $name
   ;;
  e)
   enter_env $name
   ;;
  l)
   list_envs
   ;;
  DEL)
   del_env $name
   ;;
  *)
    error "Unknown action $action"
   exit 3
   ;;
esac
  
