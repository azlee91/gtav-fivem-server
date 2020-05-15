# Grand Theft Auto V Private Server With Docker

## FX Server version: 2445 [Download latest](https://runtime.fivem.net/artifacts/fivem/build_proot_linux/master/)

### Information

This repo allows the setup of a FiveM GTAV server using `docker-compose` .

>Note: If server version is updated, change version in this README and `fivem_server/fx_server_version`

See [official server setup guide](https://docs.fivem.net/docs/server-manual/setting-up-a-server/#linux) for more information on what's going on in the background

### Scripts

Scripts that are to be added to the server should have their git repos intialized as a submodule in the `local_resources` folder. This ensures the latest updates to the scripts can be pulled easily.

### Links

Links to scripts are below:

* [mysql-async](https://github.com/brouznouf/fivem-mysql-async)
* [async](https://github.com/ESX-Org/async)
* [es_extended](https://github.com/ESX-Org/es_extended)
  * [esx_ambulancejob](https://github.com/ESX-Org/esx_ambulancejob)
  * [esx_shops](https://github.com/ESX-Org/esx_shops)
  * [esx_skin](https://github.com/ESX-Org/esx_skin)
  * [esx_vehicleshop](https://github.com/ESX-Org/esx_vehicleshop)
  * [esx_weaponshop](https://github.com/ESX-Org/esx_weaponshop)

### Usage

Run `python generate_env_file.py` to generate default SQL information

Configure server by editing `fivem_server/server.cfg` before running the following commands

Initialize the database using the following command:

`docker exec -it gta5_server_fivem_db_1 mysql -ufivem -pTOL0F2ezGExXpdKMBh4G -e "$(cat fivem_server/database_files/es_extended_db.sql)"`

Finally, run `docker-compose up -d --build` to start up the server
