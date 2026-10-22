variable "TAG" {

}

group "default" {
    targets = ["app"]
}

target "app" {
    context = "."
    dockerfile = "Dockerfile"
    platforms = ["linux/amd64", "linux/arm64"]
    tags = [
        "ghcr.io/theraphael0000/ch.scouts-bevaix.www:latest",
        "ghcr.io/theraphael0000/ch.scouts-bevaix.www:${TAG}"
    ]
    cache-from = ["type=gha"]
    cache-to = ["type=gha,mode=max"]
}