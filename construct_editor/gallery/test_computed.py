import construct as cs
import construct_typed as cst
import dataclasses
import typing as t
from . import GalleryItem


@dataclasses.dataclass
class TStructTest(cst.TContainerMixin):
    type_int: int = cst.sfield(cs.Computed(lambda ctx: 50))
    type_float: float = cst.sfield(cs.Computed(lambda ctx: 80.0))
    type_bool: bool = cst.sfield(cs.Computed(lambda ctx: True))
    type_bytes: bytes = cst.sfield(cs.Computed(lambda ctx: bytes([0x00, 0xAB])))
    type_bytearray: bytearray = cst.sfield(
        cs.Computed(lambda ctx: bytearray([0x00, 0xAB, 0xFF]))
    )


constr = cst.TStruct(TStructTest)

gallery_item = GalleryItem(
    construct=constr,
    example_binarys={"Zeros": bytes([])},
)