# parse all secrets from .env file to be acessible inside of .tf files as local.envs["KEY_NAME"]
locals {
  envs = { for tuple in regexall("(.*)=(.*)", file(".env")) : tuple[0] => sensitive(tuple[1]) }
}