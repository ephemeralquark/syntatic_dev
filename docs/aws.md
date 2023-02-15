# Deploy to AWS Lightsail
All secrets should be kept out of this repo and saved in a secure location. The secrets should be specfied as environment variables in the container.json file for the deployment.

## SQL Migration strategy

## Useful AWS lightsail command
Create Container service
```
aws lightsail create-container-service --service-name syntactic-service \
--power micro \
--scale 1
```
Monitor the state of the container as it is being created.
```
aws lightsail get-container-services --service-name syntactic-service
```

Push container images (syntactic_web and nginx)
```
aws lightsail push-container-image --service-name syntactic-service \
--label syntactic-web-container \
--image syntactic-web-container

aws lightsail push-container-image --service-name syntactic-service \
--label syntactic-nginx-container \
--image syntactic-nginx-container
```

Create a deployment
```
aws lightsail create-container-service-deployment --service-name syntactic-service \
--containers file://.config/aws/containers.json \
--public-endpoint file://.config/aws/public-endpoint.json
```