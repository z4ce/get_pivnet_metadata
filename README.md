# get_pivnet_metadata
Gets tile metadata from pivnet  without downloading a whole tile using the api link

# install
```pip3 install -r requirements.txt```

# usage

```
usage: get_pivnet_metadata.py [-h] --url URL --token TOKEN

Get tile metadata from pivnet.

optional arguments:
  -h, --help     show this help message and exit
  --url URL      download api link
  --token TOKEN  Pivnet Legacy API Token

example: ./get_pivnet_metadata.py --url 'https://network.pivotal.io/api/v2/products/elastic- runtime/releases/160817/product_files/193873/download' --token 'xxx'
````

