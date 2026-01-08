

import podman

socket_uri = "unix:///var/folders/gf/h36kjw096m14_f2vr7hbs3fr0000gq/T/podman/podman-machine-default-api.sock"



def pull_playwright(client: podman.PodmanClient):
    # client.images.pull(repository="mcr.microsoft.com/playwright:v1.57.0-noble")
    print(client.images.list(name="playwright"))
    client.images.pull(repository="mcr.microsoft.com/playwright")

def new_playwright_container(client: podman.PodmanClient, host_port: int = 3300, name: str = "playwright-server"):
    container = client.containers.run(
        image="mcr.microsoft.com/playwright:v1.57.0-noble",
        name=f"{name}-p{host_port}",
        detach=True,
        ports={"3000/tcp": host_port},
        init=True,
        # ipc_mode="host",
        # userns_mode="keep-id",
        user="pwuser",
        working_dir="/home/pwuser",
        # security_opt=[f"seccomp={seccomp_profile}"],
        # command='/bin/sh -c "npx -y playwright@1.57.0 run-server --port 3000 --host 0.0.0.0"'
        command=["npx", "-y", "playwright@1.57.0", "run-server", "--port", "3000", "--host", "0.0.0.0"]
    ) 
    # print(container.ports)
    return container


def nuke_all_containers(client: podman.PodmanClient):
    # client.containers.stop(all=True)
    containers_list = client.containers.list(all=True)
    for container in containers_list:
        print("Nuking: ", container.name)
        # container.kill
        container.remove(force=True, v=True)

        # container.stop
    # images = client.images.list()


with podman.PodmanClient(base_url=socket_uri) as client:

    if client.ping():
        # spinup 3x instances
        nuke_all_containers(client)
        pull_playwright(client)
        for new_container_count in range(3):
            host_port = 3300 + new_container_count
            new_playwright_container(client, host_port=host_port)
        
        containers_list = client.containers.list(all=True)
        for container in containers_list:
            print(container.name)
        images = client.images.list()

        for image in images:

            print(image.id)
        # nuke_all_containers(client)
