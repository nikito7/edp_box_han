> https://github.com/home-assistant/core/archive/refs/heads/master.zip

```js
vv=001
file=master.zip
url=https://github.com/home-assistant/core/archive/refs/heads/master.zip
mkdir -p /config/custom_components/modbus/
rm -rf /config/custom_components/modbus/*
cd /config/custom_components/modbus/
ls -a
pwd
wget $url
unzip $file core-master/homeassistant/components/modbus/* -j -d .
rm $file
ls -a
pwd
sed -i -e 's/\"name\": \"Modbus\",/\"name\": \"Modbus\",\n  \"version\": \"'${vv}'\",/g' manifest.json
###ha core restart
```

Dev

```js
vv=001
file=dev.zip
url=https://github.com/home-assistant/core/archive/refs/heads/dev.zip
mkdir -p /config/custom_components/modbus/
rm -rf /config/custom_components/modbus/*
cd /config/custom_components/modbus/
ls -a
pwd
wget $url
unzip $file core-dev/homeassistant/components/modbus/* -j -d .
rm $file
ls -a
pwd
sed -i -e 's/\"name\": \"Modbus\",/\"name\": \"Modbus\",\n  \"version\": \"'${vv}'\",/g' manifest.json
###ha core restart
```