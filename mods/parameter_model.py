from pydantic import BaseModel, Field
from typing import List, Literal
import ipaddress



class ContainerInterfaceModel(BaseModel):
    """container network interface model."""
    nw_name: str = Field(..., title="Network name", description="Name of the network")
    ip_address: ipaddress.IPv4Address = Field(..., title="IP address", description="IP address of the container")


class ContainerNetowrkModel(BaseModel):
    """container network model."""
    nw_name: str = Field(..., title="Network name", description="Name of the network")
    driver: Literal['bridge', 'default'] = Field(default='default', title="Network driver", description="Network driver of the network")
    subnet: ipaddress.IPv4Network = Field(..., title="Subnet", description="Subnet of the network")


class ContainerVolumeModel(BaseModel):
    """container volume model."""
    type: Literal['volume', 'bind'] = Field(..., title="Volume type", description="Name of the volume")
    source: str = Field(..., title="Volume driver", description="Volume driver of the volume")
    target: str = Field(..., title="Volume target", description="Mount path of the volume")


class RepositoryModel(BaseModel):
    """Repository model for Repository params."""
    repository_name: str = Field(..., title="Repository name", description="Name of the repository")
    branches: List[str] = Field(..., title="Branches", description="List of branches to be created")
    clone_repositories: List[str] | None = Field(default=None, title="Clone repositories", description="List of repositories to be cloned")


class ContainerModel(BaseModel):
    """Container model for Repository params."""
    container_name: str = Field(..., title="Container name", description="Name of the container")
    image: str = Field(..., title="Image name", description="Name of the image")
    ports: List[str] | None = Field(default=None, title="Export port", description="Port to be exported")
    workdir: str | None = Field(default=None, title="Work directory", description="Working directory of the container")
    volumes: List[ContainerVolumeModel] | None = Field(default=None, title="Volumes", description="List of volumes")
    command: List[str] | None = Field(default=None, title="Command", description="Command to be executed")
    netowrks: List[ContainerInterfaceModel] | None = Field(default=None, title="Interfaces", description="List of network interfaces")


class ParameterModel(BaseModel):
    """Parameter model for Repository params."""
    repository: RepositoryModel = Field(..., title="Repository", description="Repository parameters")
    container_nw: List[ContainerNetowrkModel] | None = Field(default=None, title="Networks", description="List of networks")
    containers: List[ContainerModel] = Field(..., title="Containers", description="List of containers")