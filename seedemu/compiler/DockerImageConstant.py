from .DockerImage import DockerImage
from seedemu.core import BaseSystem
from enum import Enum 

UBUNTU_IMAGE   = DockerImage(name='ubuntu:20.04',
                                software=[],
                                subset=None)

BASE_IMAGE     = DockerImage(name='handsonsecurity/seedemu-multiarch-base:buildx-latest',
                                software=['zsh', 'curl', 'nano', 'vim-nox', 'mtr-tiny', 'iproute2',
                                        'iputils-ping', 'tcpdump', 'termshark', 'dnsutils', 'jq', 'ipcalc', 'netcat'],
                                subset=UBUNTU_IMAGE)

ROUTER_IMAGE   = DockerImage(name='handsonsecurity/seedemu-multiarch-router:buildx-latest',
                                software=['bird2'],
                                subset=BASE_IMAGE)

ETHEREUM_IMAGE = DockerImage(name='handsonsecurity/seedemu-ethereum',
                                software=['software-properties-common', 'python3', 'python3-pip'],
                                subset=BASE_IMAGE)

UBUNTU_IMAGE_ARM64   = DockerImage(name='ubuntu:20.04',
                                software=[],
                                subset=None)

BASE_IMAGE_ARM64     = DockerImage(name='handsonsecurity/seedemu-multiarch-base:buildx-latest',
                                software=['zsh', 'curl', 'nano', 'vim-nox', 'mtr-tiny', 'iproute2',
                                        'iputils-ping', 'tcpdump', 'termshark', 'dnsutils', 'jq', 'ipcalc', 'netcat'],
                                subset=UBUNTU_IMAGE_ARM64)

ROUTER_IMAGE_ARM64   = DockerImage(name='handsonsecurity/seedemu-multiarch-router:buildx-latest',
                                software=['bird2'],
                                subset=BASE_IMAGE_ARM64)

ETHEREUM_IMAGE_ARM64 = DockerImage(name='handsonsecurity/seedemu-ethereum-arm64',
                                software=['software-properties-common', 'python3', 'python3-pip'],
                                subset=BASE_IMAGE_ARM64)

BASESYSTEM_DOCKERIMAGE_MAPPING = {
        BaseSystem.UBUNTU_20_04:           UBUNTU_IMAGE,
        BaseSystem.SEEDEMU_BASE:           BASE_IMAGE,
        BaseSystem.SEEDEMU_ROUTER:         ROUTER_IMAGE,
        BaseSystem.SEEDEMU_ETHEREUM:       ETHEREUM_IMAGE
}

BASESYSTEM_ARM64_DOCKERIMAGE_MAPPING = {
        BaseSystem.UBUNTU_20_04:     UBUNTU_IMAGE_ARM64,
        BaseSystem.SEEDEMU_BASE:     BASE_IMAGE_ARM64,
        BaseSystem.SEEDEMU_ROUTER:   ROUTER_IMAGE_ARM64,
        BaseSystem.SEEDEMU_ETHEREUM: ETHEREUM_IMAGE_ARM64
}

class Platform(Enum):
    """!
    @brief Platform Enum.
    """

    ARM64 = 'arm64'
    AMD64 = 'amd64'

BASESYSTEM_DOCKERIMAGE_MAPPING_PER_PLATFORM = {
    Platform.AMD64:     BASESYSTEM_DOCKERIMAGE_MAPPING,
    Platform.ARM64:     BASESYSTEM_ARM64_DOCKERIMAGE_MAPPING
}
