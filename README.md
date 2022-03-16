# Get AWS Creds for authenticated and un-authenticated access

This is a simple python script to get aws credentials in exchange for parameters. We can get aws creds for both authenticated and unauthenticated access.

![GitHub forks](https://img.shields.io/github/forks/0xAs1F/getCognitoCreds)  ![GitHub Repo stars](https://img.shields.io/github/stars/0xAs1F/getCognitoCreds)  ![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/0xAs1F/getCognitoCreds) [![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)  [![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/) [![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

## Requirements

The only requirement needed here would be AWS python SDK boto3 and python3.

## Installation



```bash
  pip install boto3

  git clone https://github.com/0xAs1F/getCognitoCreds.git

  cd getCognitoCreds/
```
    
## Usage/Examples

```python
python3 auth.py -t {id-token} -i {identity-pool-id} -u {user-pool-id} -r {aws-region} 
python3 unauth.py -p {identity-pool-id} -r {aws-region}
```


## Screenshots

- For authenticated aws credentials

    [![EtJQyv.md.png](https://iili.io/EtJQyv.md.png)](https://freeimage.host/i/EtJQyv)
    
- For un-authenticated aws credentials

    [![EtdRAx.md.png](https://iili.io/EtdRAx.md.png)](https://freeimage.host/i/EtdRAx)
    


