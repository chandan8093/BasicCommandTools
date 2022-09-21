# golden-ami

>>> golden-ami using Hashicorp Packer

* Packer is tool provided by hashicorp, used to package the machine images programatically

> Note: Make sure you have packer installed on your system and aws access configured 

*** How to use ***

- Update IRestore AWS Account ID in line 24 at packer/template.json

- build.sh file to build the image
    - Arguments to be used for script to be executed
        ```
        region=$1
        app=$2
        version=$3
        ```

* execute shell script like this
```sh build.sh <region> <appname> <version>```