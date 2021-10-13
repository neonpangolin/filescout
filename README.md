![filescout_black](https://user-images.githubusercontent.com/83586282/137082844-731cac71-a8d3-4dfb-b6a1-ff3a0f9b88a3.png)


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
<img width="476" alt="Screenshot 2021-10-13 at 09 00 04" src="https://user-images.githubusercontent.com/83586282/137083189-4ac83107-0fe0-40c1-a357-d652b9d881e7.png">


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
