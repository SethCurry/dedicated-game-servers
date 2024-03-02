# Valheim Server Configuration
## Building
First, you will need to build the base Docker image.  See the [README](../base/README.md) for instructions on how to do this.


Once you have done that, you can build the game server image with this command:

```bash
docker build . -t dgs.scurry.io/valheim:latest
```
## Configuration
### Environment Variables
| Environment Variable | Config Option | Type | Description | Default |
| --- | --- | --- | --- | --- |
| LOG_FILE | logFile | string | The file to log to | None |
| NAME | name | string | The name of the server | Valheim Server |
| PASSWORD | password | string | The password for the server | None |
| PORT | port | integer | The port the server will listen on | 2456 |
| PUBLIC | public | integer | Whether the server is public (1) or not (0) | 1 |
| SAVE_DIR | savedir | string | The directory to save the world to | None |
| WORLD | world | string | The name of the world | MyWorld |
