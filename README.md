# Get AWS Creds for authenticated and un-authenticated access

This is a simple python script to get aws credentials in exchange for parameters. We can get aws creds for both authenticated and unauthenticated access.

![GitHub forks](https://img.shields.io/github/forks/0xAs1F/getCognitoCreds)  ![GitHub Repo stars](https://img.shields.io/github/stars/0xAs1F/getCognitoCreds)  ![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/0xAs1F/getCognitoCreds) [![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)  [![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/) [![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

## Requirements

The only requirement needed here would be AWS python SDK boto3 and python.

## Installation



```bash
  pip install boto3

  git clone https://github.com/0xAs1F/getCognitoCreds.git

  cd getCognitoCreds/
```
    
## Usage/Examples

```python
python3 auth.py -t {id-token} -a {user-pool-arn} -r {aws-region} 
python3 unauth.py -p {identity-pool-id} -r {aws-region}
```


## Screenshots

![For authenticated aws creds](https://ray.so/?title=&theme=falcon&spacing=16&background=true&darkMode=true&code=cHl0aG9uMyBhdXRoLnB5IC10IGV5SnJhV1FpT2kuLi4uIC1wIHVzLWVhc3QtMjo1ZDZhZGMtYmVmLTQ5My1hYTA5LTg2YzVlOTIzMWNjOCAtYSBjb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbS91cy1lYXN0LTJfdFREZGZkZmRmaUhISSAtciB1cy1lYXN0LTE&language=julia)
![For un-authenticated aws creds](https://ray.so/?title=unauth.py&theme=falcon&spacing=16&background=true&darkMode=true&code=IHB5dGhvbjMgdW5hdXRoLnB5IC1wIHVzLWVhc3QtMTo1ZDQ0NDQ2YWRjLWIxZWYtNDExMy1hYTA5LTg2Nzg4OWNiZ2dnYzggLXIgdXMtZWFzdC0x&language=julia)


