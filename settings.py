#!/usr/bin/env python3

from os import getenv, path, makedirs
from json import loads
from shutil import copytree

home = getenv('HOME')
usr_data = f'{home}/.local/share/OneForAll/dumps/'
conf_path = f'{home}/.config/OneForAll'
path_to_script = path.dirname(path.realpath(__file__))
src_conf_path = f'{path_to_script}/conf/'
meta_file_path = f'{path_to_script}/metadata.json'
keys_file_path = f'{conf_path}/keys.json'
conf_file_path = f'{conf_path}/config.json'
log_file_path = f'{home}/.local/share/OneForAll/run.log'

if not path.exists(conf_path):
	copytree(src_conf_path, conf_path, dirs_exist_ok=True)

if not path.exists(usr_data):
	makedirs(usr_data, exist_ok=True)

with open(conf_file_path, 'r') as config_file:
	config_read = config_file.read()
	config_json = loads(config_read)
	timeout = config_json['common']['timeout']

	ssl_port = config_json['ssl_cert']['ssl_port']

	port_scan_th = config_json['port_scan']['threads']

	dir_enum_th = config_json['dir_enum']['threads']
	dir_enum_redirect = config_json['dir_enum']['redirect']
	dir_enum_sslv = config_json['dir_enum']['verify_ssl']
	dir_enum_dns = config_json['dir_enum']['dns_server']
	dir_enum_ext = config_json['dir_enum']['extension']
	dir_enum_wlist = f'{path_to_script}/wordlists/dirb_common.txt'

	export_fmt = config_json['export']['format']
