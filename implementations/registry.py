from implementations.Quickfind import QuickFind
from implementations.QuickUnion import QuickUnion


UF_REGISTRY = {
    "QuickFind": QuickFind,
    "QuickUnion": QuickUnion,
}


def get_uf_class(name: str):
    return UF_REGISTRY[name]
