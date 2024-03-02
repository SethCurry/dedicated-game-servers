# Base Configuration

## Building

First, you will need to build the base Docker image. See the [README](../base/README.md) for instructions on how to do this.

Once you have done that, you can build the game server image with this command:

```bash
docker build -t dgs.scurry.io/base:latest .
```

## Configuration

### Environment Variables

| Environment Variable | Config Option | Type | Description | Default |
| -------------------- | ------------- | ---- | ----------- | ------- |
