<p align="center"><img src="https://i.imgur.com/rLENhCp.jpg"></p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3-brightgreen.svg?style=plastic">
<img src="https://img.shields.io/badge/All In One-red.svg?style=plastic">
<img src="https://img.shields.io/badge/Web Recon-red.svg?style=plastic">
</p>

<p align="center">
  <a href="https://twitter.com/thewhiteh4t"><b>Twitter</b></a>
  <span> - </span>
  <a href="https://t.me/thewhiteh4t"><b>Telegram</b></a>
  <span> - </span>
  <a href="https://thewhiteh4t.github.io"><b>thewhiteh4t's Blog</b></a>
</p>

OneForAll is an all in one **automatic web reconnaissance** tool written in python. Goal of OneForAll is to provide an **overview** of the target in a **short** amount of time while maintaining the **accuracy** of results. Instead of executing **several tools** one after another it can provide similar results keeping dependencies **small and simple**.

## Available In

<p align="center">
  <a href="https://www.kali.org/news/kali-linux-2020-4-release/">
    <img width="150px" hspace="10px" src="https://i.imgur.com/teSiL4p.png" alt="kali linux OneForAll">
  </a>
  <a href="https://blackarch.org/">
    <img width="150px" hspace="10px" src="https://i.imgur.com/YZ5KDL1.png" alt="blackarch OneForAll">
  </a>
  <a href="https://secbsd.org/">
    <img width="150px" hspace="10px" src="https://i.imgur.com/z36xL8c.png" alt="secbsd OneForAll">
  </a>
</p>

## Featured

### Python For OSINT
* Hakin9 April 2020
* https://hakin9.org/product/python-for-osint-tooling/

### NullByte
* https://null-byte.wonderhowto.com/how-to/conduct-recon-web-target-with-python-tools-0198114/
* https://www.youtube.com/watch?v=F9lwzMPGIgo

### Hakin9
* https://hakin9.org/final-recon-osint-tool-for-all-in-one-web-reconnaissance/

## Features

OneForAll provides detailed information such as :

* Header Information

* Whois

* SSL Certificate Information

* Crawler
  * html
    * CSS
    * Javascripts
    * Internal Links
    * External Links
    * Images
  * robots
  * sitemaps
  * Links inside Javascripts
  * Links from Wayback Machine from Last 1 Year

* DNS Enumeration
  * A, AAAA, ANY, CNAME, MX, NS, SOA, TXT Records
  * DMARC Records

* Subdomain Enumeration
  * Data Sources
    * BuffOver
    * crt.sh
    * ThreatCrowd
    * AnubisDB
    * ThreatMiner
    * Facebook Certificate Transparency API
      * Auth Token is Required for this source, read Configuration below
    * VirusTotal
    	* API Key is Required
    * Shodan
      * API Key is Required
    * CertSpotter

* Directory Searching
  * Support for File Extensions

* Wayback Machine
    * URLs from Last 5 Years

* Port Scan
  * Fast
  * Top 1000 Ports

* Export
  * Formats
    * txt
    * json [Coming Soon]

## Configuration

### API Keys

Some Modules Use API Keys to fetch data from different resources, these are optional, if you are not using an API key, they will be simply skipped.
If you are interested in using these resources you can store your API key in **keys.json** file.

`Path --> $HOME/.config/OneForAll/keys.json`

If you don't want to use a key for a certain data source just set its value to `null`, by default values of all available data sources are null.

#### Facebook Developers API

This data source is used to fetch **Certificate Transparency** data which is used in **Sub Domain Enumeration**

Key Format : `APP-ID|APP-SECRET`

Example :

```
{
  "facebook": "9go1kx9icpua5cm|20yhraldrxt6fi6z43r3a6ci2vckkst3"
}
```

Read More : https://developers.facebook.com/docs/facebook-login/access-tokens

#### VirusTotal API

This data source is used to fetch **Sub Domains** which are used in **Sub Domain Enumeration**

Key Format : `KEY`

Example :

```
{
	"virustotal": "eu4zc5f0skv15fnw54nkhj4m26zbteh9409aklpxhfpp68s8d4l63pn13rsojt9y"
}
```

#### Shodan API

This data source is used to fetch **Sub Domains** which are used in **Sub Domain Enumeration**

Key Format : `KEY`

Example :

```
{
	"shodan": "eu4zc5f0skv15fnw54nkhj"
}
```

#### BeVigil API

This data source is used to fetch **Sub Domains** which are used in **Sub Domain Enumeration**

Key Format : `KEY`

Example :

```
{
	"bevigil": "bteh9409aklpxhfpp68s8d"
}
```


## Tested on

* Kali Linux
* BlackArch Linux

> OneForAll is a tool for **Pentesters** and it's designed for **Linux** based Operating Systems, other platforms like **Windows** and **Termux** are **NOT** supported.

## Installation

### Kali Linux

```
sudo apt install OneForAll
```

### BlackArch Linux

```
sudo pacman -S OneForAll
```

### SecBSD

```bash
doas pkg_add OneForAll
```

### Other Linux

```bash
git clone https://github.com/thewhiteh4t/OneForAll.git
cd OneForAll
pip3 install -r requirements.txt
```

### Docker

``` bash
docker pull thewhiteh4t/OneForAll
docker run -it --entrypoint /bin/sh thewhiteh4t/OneForAll
```

Also docker user can use this alias to run the OneForAll as the normal CLI user.

``` bash
alias OneForAll="docker run -it --rm --name OneForAll  --entrypoint 'python3' thewhiteh4t/OneForAll OneForAll.py"
```

And then use `OneForAll` to start your scan.

> remark
>
> If you have any api keys you can easily commit that image in your local machine.
>
> This docker usage needs root to run docker command.

## Usage

```bash
usage: OneForAll.py [-h] [--headers] [--sslinfo] [--whois] [--crawl]
                     [--dns] [--sub] [--dir] [--wayback] [--ps]
                     [--full] [-dt DT] [-pt PT] [-T T] [-w W] [-r]
                     [-s] [-sp SP] [-d D] [-e E] [-o O]
                     url

OneForAll - The Last Web Recon Tool You Will Need | v1.1.5

positional arguments:
  url         Target URL

options:
  -h, --help  show this help message and exit
  --headers   Header Information
  --sslinfo   SSL Certificate Information
  --whois     Whois Lookup
  --crawl     Crawl Target
  --dns       DNS Enumeration
  --sub       Sub-Domain Enumeration
  --dir       Directory Search
  --wayback   Wayback URLs
  --ps        Fast Port Scan
  --full      Full Recon

Extra Options:
  -dt DT      Number of threads for directory enum [ Default : 30 ]
  -pt PT      Number of threads for port scan [ Default : 50 ]
  -T T        Request Timeout [ Default : 30.0 ]
  -w W        Path to Wordlist [ Default : wordlists/dirb_common.txt
              ]
  -r          Allow Redirect [ Default : False ]
  -s          Toggle SSL Verification [ Default : True ]
  -sp SP      Specify SSL Port [ Default : 443 ]
  -d D        Custom DNS Servers [ Default : 1.1.1.1 ]
  -e E        File Extensions [ Example : txt, xml, php ]
  -o O        Export Format [ Default : txt ]
```

```bash
# Check headers

python3 OneForAll.py --headers <url>

# Check ssl Certificate

python3 OneForAll.py --sslinfo <url>

# Check whois Information

python3 OneForAll.py --whois <url>

# Crawl Target

python3 OneForAll.py --crawl <url>

# Directory Searching

python3 OneForAll.py --dir <url> -e txt,php -w /path/to/wordlist

# full scan

python3 OneForAll.py --full <url>
```

## Demo
[![Odysee](https://i.imgur.com/IQpZ67e.png)](https://odysee.com/@thewhiteh4t:2/what%27s-new-in-OneForAll-v1.0.2-osint:c)
