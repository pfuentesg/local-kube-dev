# Local kubernetes development

This repo contains the code and steps to reproduce locla kubernetes development presentation by [Pablo Fuentes](linkedin.com/in/pablo-fuentes/)

Both microservices and configs are located under its folders (api-micro and api-store)

## Develop with telepresence (v2)

We'll work with [Telepresence v2](https://www.getambassador.io/docs/telepresence/)

Please, make sure you have telepresence [Installed](https://www.getambassador.io/docs/telepresence/latest/howtos/intercepts/#1-install-the-telepresence-cli) before running it

If you type `telepresence connect`you will be able to connect to the api (from the ambasador ns) as like with your local machine

## Develop with Okteto 

We'll work with [Okteto](https://okteto.com/)

Please, make sure you have okteto cli [Installed](https://okteto.com/docs/getting-started/installation) before running it

If you type `okteto up` the env will load automatically. You don't have the okteto.yml file for your app? don´t worry! just type `okteto up` and follow the steps to create it or check their [reference](https://okteto.com/docs/reference/stacks)

## Develop qwith skaffold

We'll work with [Skaffold](https://skaffold.dev/)

Please, make sure you have skaffold cli [Installed](https://skaffold.dev/docs/install/) before running it


If you type `skaffold dev --port-forward` you will be able t to run the application, with your local code and a port forward to the app in the cluster. If you need more help with the configuration, check [their reference](https://skaffold.dev/docs/references/yaml/) or follow their [guides](https://skaffold.dev/docs/quickstart/)

Please, note that if you are not working with minikube, the docker image should be built and pushed on each change (so you will need access to the docker registry)
