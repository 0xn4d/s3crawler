# s3crawler

This tool was developed to bug hunter and pentesters.

## Instalation

```git clone https://github.com/daniloalbuqrque/s3crawler```

```cd s3crawler```

```pip3 install -r requirements```

## Usage

```python3 s3crawler domain_subdomains_and_endpoints.txt```

Using this command, you will be able to analyze all the **valid** websites' source codes searching for hard coded Buckets S3 links. With that, you can test for Bucket S3 Takeover vulnerabilities.
