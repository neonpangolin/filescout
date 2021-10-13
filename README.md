![filescout_logo](https://user-images.githubusercontent.com/83586282/137083724-27d6284a-6758-4003-aee5-b899aaf61ea3.png)

# Filescout

### Introduction
A minimalistic OSINT utility, designed to expedite file lookups on any given website.
Depending on the selected flag, Filescout will send multiple request to Google.com, which may result in captchas issues - please allow time between searches.

### Rquirements

• requests

• webbrowser

### Usage
```
git clone https://github.com/aleksanderklug/filescout.git
cd filescout
python3 filescout.py
```

### Example
<img width="487" alt="filescout_usage" src="https://user-images.githubusercontent.com/83586282/137083690-4461f584-f344-4c25-bbb2-f83cb41ba131.png">

### Supported filetypes

Documents

- txt, rtf, odt, csv, xls, xlsx, odp, ppt, html, mht, xml

Passwords

- htpasswd, pass, password, pem, csr, netrc, key, pgp, asc

Emails 

- eml, mbx, wab

Databases

- sql, nsf, php, mdb, fp3, fp5, fp7, ldb, ora, myd

Software 

- env, inf, cfg, log, dotenv, inf, ini, lic, blt, conf, log, reg, env, mdb, cfm, config, avastlic

Configurations

- ns1, pac, pcf, cfm, axd, cgi, cnf, jnlp, pcmcfg, mobileconfig

Microsoft:

- lit, ldb, mdb, mny, pdb, bkf
