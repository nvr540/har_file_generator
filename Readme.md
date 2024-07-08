# Har_file Generator

The Project uses selenium and Browsemob-proxy to intercept the request sent by a website.

It uses MITM to capture the data and saves it in an ```HAR_FILE.```


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requiremnets.txt
```

## Usage

```bash
python selenium2_auto.py
```

## Prerequisite

You may have to change the path of the browser mob-proxy.bat file. It sometimes doesn't work if the full path is not provided.

Also, you must add the certificate in your Chrome browser to capture the data or it can't. ``` You should remove the certificates after use````.
## Adding Certificates.

You will get the certificates in the browsermob-proxy-2.1.4-bin folder in ```ssl-support``` sub-folder.

You must add both the file 
1. ```ca-certificate-ec.cer```
2. ```ca-certificate-rsa.cer```

## Har File

All the traffic will be saved in in ```network_traffic.json```.#   h a r _ f i l e _ g e n e r a t o r 
 
 
