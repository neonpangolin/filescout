# Filescout

### Introduction
A minimalistic OSINT utility, designed to expedite file lookups on any given website.
Depending on the selected flag, Filescout will send multiple request to Google.com, which may result in captchas issues - there, please allow time between searches.

### Rquirements

• requests

• webbrowser

### Usage
```
git clone https://github.com/aleksanderklug/filescout.git
cd filescout
python3 filescout.py
```

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
