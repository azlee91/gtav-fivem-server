# Grand Theft Auto V Private Server With Docker

## FX Server version: 2445 ([Download Latest](https://runtime.fivem.net/artifacts/fivem/build_proot_linux/master/))

>:information_source: Note: If server version is updated, change version in this README and `fivem_server/fx_server_version`

## Information

This repo allows the setup of a FiveM GTAV server using `docker-compose` .

See [official server setup guide](https://docs.fivem.net/docs/server-manual/setting-up-a-server/#linux) for more information on what's going on in the background

## Links

The following scripts are included in this server:

* [mysql-async](https://github.com/brouznouf/fivem-mysql-async)
* [async](https://github.com/ESX-Org/async)
* [es_extended](https://github.com/ESX-Org/es_extended)
  * [esx_ambulancejob](https://github.com/ESX-Org/esx_ambulancejob)
  * [esx_shops](https://github.com/ESX-Org/esx_shops)
  * [esx_skin](https://github.com/ESX-Org/esx_skin)
  * [esx_vehicleshop](https://github.com/ESX-Org/esx_vehicleshop)
  * [esx_weaponshop](https://github.com/ESX-Org/esx_weaponshop)

---

## First Start Usage

Follow these steps when starting the server for the first time.

Run `python generate_env_file.py` to generate default SQL information

Configure server by editing `fivem_server/server.cfg` before running the following commands
>:information_source: Note: Make sure to replace the username/password/database in the db connect string

Run `$ docker-compose up -d --build` to start up the server

Wait a minute and initialize the database using the following command:

```bash
$ docker exec -it gta5_server_fivem_db_1 mysql -u[username] -p[mysql_password] -e "$(cat fivem_server/database_files/es_extended_db.sql)"
```

Finally, restart the FiveM server container using `$ docker-compose restart fivem_server` so it can connect to the DB

That's it! :tada: Start up the FiveM client and connect to the server!

## Adding Scripts/Mods

See [Script/Mod README](fivem_server/local_resources/README.md)

---

## Docker Notes

The docker container for the MySQL DB is mounted on a volume and not bind mounted. This means that the data is stored in an internal volume in docker. When you stop/start/recreate the MySQL container, the SQL data is retained.
>:information_source: Note: See FAQ section for information on how to remove the volume

## F.A.Q

>:question: Q: I've messed up and need to start over, how do I do that?

Run `$ docker-compose down --volumes` to tear down the stack. `--volumes` tells docker to also remove the mounted volumes.

>:warning: Warning: Removing the volumes will cause you to lose all data! (This includes database data). Make sure to backup your database if you plan on removing the volumes

>:question: Q: How do I backup my database?

Run the following command:

```bash
$ docker exec gta5_server_fivem_db_1 sh -c 'exec mysqldump --all-databases -u[username] -p[mysql_password]' > /some/path/on/your/host/all-databases.sql
```

>:question: Q: Ok I've backed up my DB, now how do I restore that backup?

Run the following command:

```bash
$ docker exec -i some-mysql sh -c 'exec mysql -u[username] -p[mysql_password]' < /some/path/on/your/host/all-databases.sql
```
